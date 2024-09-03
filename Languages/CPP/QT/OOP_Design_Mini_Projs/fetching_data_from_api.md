### Report on MainWindow Implementation

#### Objective
The objective of this small project was to create a Qt application that fetches data from a REST API and displays it using two different types of widgets: `QListWidget` and `QFormLayout`. This project aimed to explore various aspects of Qt for displaying data, managing network requests, and designing user interfaces.

#### Aspects of Qt Covered

1. **Network Requests**:
   - Utilized `QNetworkAccessManager` for making asynchronous HTTP requests to fetch data from a REST API.
   - Managed `QNetworkReply` to handle responses and errors.

2. **Widgets and Layouts**:
   - **`QListWidget`**: Used to display data in a list format. Demonstrates how to add, remove, and manage items within the widget.
   - **`QFormLayout`**: Used within a container widget to display key-value pairs. This shows how to dynamically add form rows based on fetched data.
   - **`QLineEdit`**: Allows user input for the API request.
   - **`QPushButton`**: Triggers the data fetching process.
   - **`QLabel`**: Used for headers and displaying static text with custom styling.
   - **`QTextEdit`**: Displays multiline text and is set to read-only.

3. **Styling**:
   - Applied custom styles to `QLabel` headers to enhance visual appearance using Qt’s stylesheet system.

4. **Dynamic UI Management**:
   - Managed dynamic content updates in the UI based on the fetched data.
   - Cleared previous items in the `QFormLayout` before adding new ones to avoid clutter.

#### Explanation of Code

1. **Initialization**:
   - A `QMainWindow` derived class `MainWindow` is initialized.
   - `QWidget` is set as the central widget with a vertical box layout (`QVBoxLayout`) for organizing child widgets.

2. **Creating and Setting Widgets**:
   - **`QListWidget`**: Added to the layout to display data in a list format.
   - **`QFormLayout`**: Used within a `QWidget` container to show key-value pairs fetched from the API.
   - **`QPushButton`** and **`QLineEdit`**: Added for user interaction.

3. **Button Click Handling**:
   - Connected the `QPushButton`’s `clicked` signal to the `fetchData` function, which triggers data fetching when the button is pressed.

4. **Fetching Data**:
   - In the `fetchData` function:
     - **Network Request**: A `QNetworkAccessManager` instance is created to make a GET request to the API using the URL constructed from user input.
     - **Data Parsing**: The response data is parsed as JSON and converted to `QString` for display.
     - **Updating UI**:
       - **`QListWidget`**: Clears previous items and adds new ones based on the response.
       - **`QFormLayout`**: Clears previous rows and adds new rows with fetched data. The `QTextEdit` widget is used to display large text data like the body of the response.

5. **Memory Management**:
   - Deleted layout items and widgets as part of cleaning up to prevent memory leaks.

#### Summary
This project demonstrates essential Qt concepts such as handling network requests, managing different types of widgets, and dynamically updating UI elements. It provides practical experience with `QListWidget`, `QFormLayout`, `QPushButton`, `QLineEdit`, and data handling in Qt applications. The application showcases how to create a responsive and interactive UI that fetches and displays data from an API, providing a foundational understanding of building Qt-based applications.

## Codes

`mainwidow.cpp`

```cpp
#include "mainwindow.h"
#include <QVBoxLayout>
#include <QWidget>
#include <QPushButton>
#include <QtNetwork/QNetworkAccessManager>
#include <QtNetwork/QNetworkReply>
#include <QUrl>
#include <QJsonDocument>
#include <QJsonObject>
#include <QDebug>
#include <QLineEdit>
#include <QListWidget>
#include <QFormLayout>
#include <QLabel>
#include <QTextEdit>


void fetchData(QLineEdit*, QListWidget*, QFormLayout*);


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    QWidget *centralWidget = new QWidget(this);
    this->setWindowTitle("Basic Application With chumma HTTP Request");
    setCentralWidget(centralWidget);



    QListWidget *listWidget = new QListWidget();
    QFormLayout *formLayout = new QFormLayout(this);

    QWidget *formContainer = new QWidget();
    formContainer->setLayout(formLayout);

    QPushButton *btn1 = new QPushButton("Fetch Data");
    QLineEdit *inp1 = new QLineEdit();

    QVBoxLayout *layout = new QVBoxLayout(centralWidget);
    layout->addWidget(inp1);
    layout->addWidget(btn1);
    QLabel *label1 = new QLabel("Displaying using QListWidget");
    label1->setStyleSheet("font-size: 18px; font-weight: bold; color: #0078D7; border-bottom: 2px solid #0078D7; padding-bottom: 5px;");
    layout->addWidget(label1);
    layout->addWidget(listWidget);

    QLabel *label2 = new QLabel("Displaying using QListWidget");
    label2->setStyleSheet("font-size: 18px; font-weight: bold; color: #0078D7; border-bottom: 2px solid #0078D7; padding-bottom: 5px;");
    layout->addWidget(label2);

    layout->addWidget(formContainer);



    QObject::connect(btn1, &QPushButton::clicked, [this, inp1, listWidget, formLayout](){
        fetchData(inp1, listWidget, formLayout);
    });



}


void fetchData(QLineEdit *inp1, QListWidget *listWidget, QFormLayout *formLayout) {

    qDebug() << "Going to fetch Data";

    // Create a network access manager
    QNetworkAccessManager *manager = new QNetworkAccessManager();

    // getting data from input field

    QString inputVal = inp1->text();

    QUrl url("https://jsonplaceholder.typicode.com/posts/"+inputVal);

    QNetworkRequest request(url);

    QObject::connect(manager, &QNetworkAccessManager::finished, [=](QNetworkReply *reply) {
        if(reply->error() == QNetworkReply::NoError) {
            QByteArray responseData = reply->readAll();

            // Parsing Json Data
            QJsonDocument jsonResponse = QJsonDocument::fromJson(responseData);
            QJsonObject jsonObject = jsonResponse.object();

            qDebug() << "Response Data: \n" << jsonObject;
            qDebug() << jsonObject.value("userId").toDouble();
            qDebug() << jsonObject.value("id").toDouble();
            qDebug() << jsonObject.value("title").toString();
            qDebug() << jsonObject.value("body").toString();

            // Convert values to QString
            QString userId = QString::number(jsonObject.value("userId").toDouble());
            QString id = QString::number(jsonObject.value("id").toDouble());
            QString title = jsonObject.value("title").toString();
            QString body = jsonObject.value("body").toString();




            // clear the layout
            qDebug() << "Going to clear listWidget";
            listWidget->clear();
            listWidget->addItem("User Id: " + userId);
            listWidget->addItem("ID: " + id);
            listWidget->addItem("title: " + title);
            listWidget->addItem("body: " + body);

            // This is not looking good:

            // Clear previous form layout items
            QLayoutItem* item;
            while ((item = formLayout->takeAt(0))) {
                delete item->widget();  // Delete widget
                delete item;            // Delete layout item
            }


            formLayout->addRow("User Id: ", new QLabel(userId));
            formLayout->addRow("ID: ", new QLabel(id));
            formLayout->addRow("Title: ", new QLabel(title));

            QTextEdit *bodyText = new QTextEdit();
            bodyText->setText(body);
            bodyText->setReadOnly(true);

            formLayout->addRow(bodyText);



        }else {
            qDebug() << "Error occured: " << reply->errorString();
        }

        reply->deleteLater();
    }
);

    manager->get(request);
}

MainWindow::~MainWindow() {}

```

`main.cpp`

```cpp
#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}

```

### Output

![image](https://github.com/user-attachments/assets/1a22943a-db7e-4d50-a661-0debcad368a3)

