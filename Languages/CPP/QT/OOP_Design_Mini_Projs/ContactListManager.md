Let's create a Qt application for managing a contact list using a MySQL database. The application will connect to the MySQL database using `QSql`, and it will include separate classes for the main window UI and database operations.

### File Structure:
- `main.cpp`
- `MainWindow.h`
- `MainWindow.cpp`
- `DatabaseManager.h`
- `DatabaseManager.cpp`

## UML Diagram

```
+---------------------+
|      MainWindow     |
+---------------------+
| - nameInput: QLineEdit       |
| - phoneInput: QLineEdit      |
| - emailInput: QLineEdit      |
| - addButton: QPushButton    |
| - deleteButton: QPushButton |
| - contactTable: QTableWidget |
| - dbManager: DatabaseManager |
+---------------------+
| + addContact(): void        |
| + loadContacts(): void      |
| + deleteContact(): void     |
+---------------------+

           |
           |
           v

+---------------------+
|  DatabaseManager    |
+---------------------+
| - db: QSqlDatabase         |
+---------------------+
| + addContact(name: QString, |
|   phone: QString, email: QString): bool |
| + getContacts(): QList<QList<QString>> |
| + deleteContact(name: QString): bool |
+---------------------+

```

### Database Schema:
The MySQL database will have a table named `contacts` with the following columns:
- `id` (INT, Primary Key, Auto Increment)
- `name` (VARCHAR)
- `phone` (VARCHAR)
- `email` (VARCHAR)

### `main.cpp`
```cpp
#include <QApplication>
#include "MainWindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    MainWindow window;
    window.show();
    return app.exec();
}
```

### `MainWindow.h`
```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTableWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include "DatabaseManager.h"

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void addContact();
    void loadContacts();
    void deleteContact();

private:
    QLineEdit *nameInput;
    QLineEdit *phoneInput;
    QLineEdit *emailInput;
    QPushButton *addButton;
    QPushButton *deleteButton;
    QTableWidget *contactTable;

    DatabaseManager *dbManager;
};

#endif // MAINWINDOW_H
```

### `MainWindow.cpp`
```cpp
#include "MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), dbManager(new DatabaseManager()) {

    // Create UI components
    nameInput = new QLineEdit(this);
    phoneInput = new QLineEdit(this);
    emailInput = new QLineEdit(this);
    addButton = new QPushButton("Add Contact", this);
    deleteButton = new QPushButton("Delete Contact", this);
    contactTable = new QTableWidget(this);

    // Set placeholders
    nameInput->setPlaceholderText("Name");
    phoneInput->setPlaceholderText("Phone Number");
    emailInput->setPlaceholderText("Email");

    // Set table properties
    contactTable->setColumnCount(3);
    QStringList headers;
    headers << "Name" << "Phone" << "Email";
    contactTable->setHorizontalHeaderLabels(headers);
    contactTable->setSelectionBehavior(QTableWidget::SelectRows);
    contactTable->setSelectionMode(QTableWidget::SingleSelection);

    // Set layout
    QVBoxLayout *layout = new QVBoxLayout();
    layout->addWidget(nameInput);
    layout->addWidget(phoneInput);
    layout->addWidget(emailInput);
    layout->addWidget(addButton);
    layout->addWidget(contactTable);
    layout->addWidget(deleteButton);

    QWidget *centralWidget = new QWidget(this);
    centralWidget->setLayout(layout);
    setCentralWidget(centralWidget);

    // Connect signals to slots
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addContact);
    connect(deleteButton, &QPushButton::clicked, this, &MainWindow::deleteContact);

    // Load contacts from database
    loadContacts();
}

MainWindow::~MainWindow() {
    delete dbManager;
}

void MainWindow::addContact() {
    QString name = nameInput->text();
    QString phone = phoneInput->text();
    QString email = emailInput->text();

    if (!name.isEmpty() && !phone.isEmpty() && !email.isEmpty()) {
        dbManager->addContact(name, phone, email);
        loadContacts();
    }
}

void MainWindow::loadContacts() {
    contactTable->setRowCount(0);
    QList<QList<QString>> contacts = dbManager->getContacts();

    for (int i = 0; i < contacts.size(); ++i) {
        contactTable->insertRow(i);
        for (int j = 0; j < 3; ++j) {
            contactTable->setItem(i, j, new QTableWidgetItem(contacts[i][j]));
        }
    }
}

void MainWindow::deleteContact() {
    int currentRow = contactTable->currentRow();
    if (currentRow >= 0) {
        QString name = contactTable->item(currentRow, 0)->text();
        dbManager->deleteContact(name);
        loadContacts();
    }
}
```

### `DatabaseManager.h`
```cpp
#ifndef DATABASEMANAGER_H
#define DATABASEMANAGER_H

#include <QSqlDatabase>
#include <QSqlQuery>
#include <QSqlError>
#include <QList>
#include <QString>

class DatabaseManager {
public:
    DatabaseManager();
    ~DatabaseManager();

    bool addContact(const QString &name, const QString &phone, const QString &email);
    QList<QList<QString>> getContacts();
    bool deleteContact(const QString &name);

private:
    QSqlDatabase db;
    void initializeDatabase();
};

#endif // DATABASEMANAGER_H
```

### `DatabaseManager.cpp`
```cpp
#include "DatabaseManager.h"
#include <QDebug>

DatabaseManager::DatabaseManager() {
    db = QSqlDatabase::addDatabase("QMYSQL");
    db.setHostName("localhost");
    db.setDatabaseName("contacts_db");
    db.setUserName("root");
    db.setPassword("password");

    if (!db.open()) {
        qDebug() << "Failed to connect to MySQL database:" << db.lastError().text();
    } else {
        initializeDatabase();
    }
}

DatabaseManager::~DatabaseManager() {
    db.close();
}

void DatabaseManager::initializeDatabase() {
    QSqlQuery query;
    query.exec("CREATE TABLE IF NOT EXISTS contacts ("
               "id INT PRIMARY KEY AUTO_INCREMENT, "
               "name VARCHAR(255), "
               "phone VARCHAR(255), "
               "email VARCHAR(255))");
}

bool DatabaseManager::addContact(const QString &name, const QString &phone, const QString &email) {
    QSqlQuery query;
    query.prepare("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)");
    query.addBindValue(name);
    query.addBindValue(phone);
    query.addBindValue(email);
    return query.exec();
}

QList<QList<QString>> DatabaseManager::getContacts() {
    QList<QList<QString>> contacts;
    QSqlQuery query("SELECT name, phone, email FROM contacts");

    while (query.next()) {
        QList<QString> contact;
        contact << query.value(0).toString() << query.value(1).toString() << query.value(2).toString();
        contacts.append(contact);
    }

    return contacts;
}

bool DatabaseManager::deleteContact(const QString &name) {
    QSqlQuery query;
    query.prepare("DELETE FROM contacts WHERE name = ?");
    query.addBindValue(name);
    return query.exec();
}
```

### Explanation:
- **MainWindow**: Handles the UI, allowing users to add, view, and delete contacts. It includes:
  - `QLineEdit` widgets for name, phone, and email input.
  - A `QTableWidget` to display the list of contacts.
  - `QPushButton` widgets to trigger adding or deleting contacts.

- **DatabaseManager**: Handles all database operations. It connects to a MySQL database and provides functions for adding, retrieving, and deleting contacts. This class abstracts the database operations, providing a clean interface for the `MainWindow` to interact with.

- **Database Connection**: The application connects to a MySQL database using `QSql`. The database should be running, and the credentials (username, password, etc.) should be correctly configured.

This application is practical for managing a small contact list and demonstrates the integration of a Qt application with a MySQL database using OOP principles.
