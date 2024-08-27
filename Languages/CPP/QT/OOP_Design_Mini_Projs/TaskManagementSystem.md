Let's build a **Task Management System** where users can create, manage, and track tasks. The application will feature a complex UI with multiple components, all created programmatically in CLion.

### Key Features:
- **Task Management**: Users can add, edit, delete, and mark tasks as complete.
- **Task Categories**: Users can categorize tasks (e.g., Work, Personal, Urgent).
- **Due Dates**: Users can assign due dates to tasks and filter tasks by due date.
- **Search Functionality**: Users can search tasks by title or description.
- **Database Integration**: Use MySQL for persistent storage of tasks.

### File Structure:
- `main.cpp`
- `MainWindow.h`
- `MainWindow.cpp`
- `Task.h`
- `Task.cpp`
- `TaskManager.h`
- `TaskManager.cpp`
- `DatabaseManager.h`
- `DatabaseManager.cpp`

### Class Overview:
- **MainWindow**: Manages the main UI components and interactions.
- **Task**: Represents a task with properties like title, description, due date, etc.
- **TaskManager**: Manages a collection of `Task` objects, handling operations like adding, deleting, and searching.
- **DatabaseManager**: Handles database connections and operations using MySQL.

### UI Components:
- **Task List**: Displays tasks in a `QListWidget` or `QTableWidget`.
- **Task Details**: A separate section with `QLineEdit`, `QTextEdit`, and `QDateEdit` for viewing and editing selected tasks.
- **Category Filters**: A `QComboBox` to filter tasks by category.
- **Search Bar**: A `QLineEdit` for searching tasks by title or description.
- **Buttons**: Buttons for adding, editing, deleting tasks, and marking tasks as complete.

### Code Implementation

#### `main.cpp`
```cpp
#include <QApplication>
#include "MainWindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    MainWindow mainWindow;
    mainWindow.show();
    return app.exec();
}
```

#### `MainWindow.h`
```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidget>
#include <QLineEdit>
#include <QTextEdit>
#include <QComboBox>
#include <QPushButton>
#include <QDateEdit>
#include "TaskManager.h"

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void addTask();
    void editTask();
    void deleteTask();
    void markTaskComplete();
    void filterTasks();
    void searchTasks();
    void loadTasks();
    void selectTask(QListWidgetItem *item);

private:
    QListWidget *taskList;
    QLineEdit *taskTitle;
    QTextEdit *taskDescription;
    QDateEdit *taskDueDate;
    QComboBox *taskCategory;
    QComboBox *filterCategory;
    QLineEdit *searchBar;
    QPushButton *addButton;
    QPushButton *editButton;
    QPushButton *deleteButton;
    QPushButton *completeButton;

    TaskManager *taskManager;
};

#endif // MAINWINDOW_H
```

#### `MainWindow.cpp`
```cpp
#include "MainWindow.h"
#include <QVBoxLayout>
#include <QHBoxLayout>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), taskManager(new TaskManager()) {

    // UI Components
    taskList = new QListWidget(this);
    taskTitle = new QLineEdit(this);
    taskDescription = new QTextEdit(this);
    taskDueDate = new QDateEdit(this);
    taskCategory = new QComboBox(this);
    filterCategory = new QComboBox(this);
    searchBar = new QLineEdit(this);
    addButton = new QPushButton("Add Task", this);
    editButton = new QPushButton("Edit Task", this);
    deleteButton = new QPushButton("Delete Task", this);
    completeButton = new QPushButton("Mark as Complete", this);

    // Populate categories
    taskCategory->addItems({"Work", "Personal", "Urgent"});
    filterCategory->addItems({"All", "Work", "Personal", "Urgent"});

    // Layouts
    QVBoxLayout *leftLayout = new QVBoxLayout();
    leftLayout->addWidget(filterCategory);
    leftLayout->addWidget(taskList);
    leftLayout->addWidget(searchBar);

    QVBoxLayout *rightLayout = new QVBoxLayout();
    rightLayout->addWidget(taskTitle);
    rightLayout->addWidget(taskDescription);
    rightLayout->addWidget(taskDueDate);
    rightLayout->addWidget(taskCategory);
    rightLayout->addWidget(addButton);
    rightLayout->addWidget(editButton);
    rightLayout->addWidget(deleteButton);
    rightLayout->addWidget(completeButton);

    QHBoxLayout *mainLayout = new QHBoxLayout();
    mainLayout->addLayout(leftLayout);
    mainLayout->addLayout(rightLayout);

    QWidget *centralWidget = new QWidget(this);
    centralWidget->setLayout(mainLayout);
    setCentralWidget(centralWidget);

    // Signal-slot connections
    connect(addButton, &QPushButton::clicked, this, &MainWindow::addTask);
    connect(editButton, &QPushButton::clicked, this, &MainWindow::editTask);
    connect(deleteButton, &QPushButton::clicked, this, &MainWindow::deleteTask);
    connect(completeButton, &QPushButton::clicked, this, &MainWindow::markTaskComplete);
    connect(filterCategory, &QComboBox::currentTextChanged, this, &MainWindow::filterTasks);
    connect(searchBar, &QLineEdit::textChanged, this, &MainWindow::searchTasks);
    connect(taskList, &QListWidget::itemClicked, this, &MainWindow::selectTask);

    // Load tasks from the database
    loadTasks();
}

MainWindow::~MainWindow() {
    delete taskManager;
}

void MainWindow::addTask() {
    QString title = taskTitle->text();
    QString description = taskDescription->toPlainText();
    QDate dueDate = taskDueDate->date();
    QString category = taskCategory->currentText();

    if (!title.isEmpty()) {
        taskManager->addTask(Task(title, description, dueDate, category));
        loadTasks();
    }
}

void MainWindow::editTask() {
    // Editing logic here
}

void MainWindow::deleteTask() {
    // Deletion logic here
}

void MainWindow::markTaskComplete() {
    // Mark task complete logic here
}

void MainWindow::filterTasks() {
    // Filtering logic here
}

void MainWindow::searchTasks() {
    // Searching logic here
}

void MainWindow::loadTasks() {
    taskList->clear();
    QList<Task> tasks = taskManager->getTasks();

    foreach (Task task, tasks) {
        QListWidgetItem *item = new QListWidgetItem(task.getTitle());
        item->setData(Qt::UserRole, task.getId());
        taskList->addItem(item);
    }
}

void MainWindow::selectTask(QListWidgetItem *item) {
    int taskId = item->data(Qt::UserRole).toInt();
    Task task = taskManager->getTaskById(taskId);

    taskTitle->setText(task.getTitle());
    taskDescription->setText(task.getDescription());
    taskDueDate->setDate(task.getDueDate());
    taskCategory->setCurrentText(task.getCategory());
}
```

#### `Task.h`
```cpp
#ifndef TASK_H
#define TASK_H

#include <QString>
#include <QDate>

class Task {
public:
    Task(const QString &title, const QString &description, const QDate &dueDate, const QString &category);

    int getId() const;
    QString getTitle() const;
    QString getDescription() const;
    QDate getDueDate() const;
    QString getCategory() const;

    void setId(int id);
    void setTitle(const QString &title);
    void setDescription(const QString &description);
    void setDueDate(const QDate &dueDate);
    void setCategory(const QString &category);

private:
    int id;
    QString title;
    QString description;
    QDate dueDate;
    QString category;
};

#endif // TASK_H
```

#### `Task.cpp`
```cpp
#include "Task.h"

Task::Task(const QString &title, const QString &description, const QDate &dueDate, const QString &category)
    : title(title), description(description), dueDate(dueDate), category(category), id(-1) {}

int Task::getId() const { return id; }
QString Task::getTitle() const { return title; }
QString Task::getDescription() const { return description; }
QDate Task::getDueDate() const { return dueDate; }
QString Task::getCategory() const { return category; }

void Task::setId(int id) { this->id = id; }
void Task::setTitle(const QString &title) { this->title = title; }
void Task::setDescription(const QString &description) { this->description = description; }
void Task::setDueDate(const QDate &dueDate) { this->dueDate = dueDate; }
void Task::setCategory(const QString &category) { this->category = category; }
```

#### `TaskManager.h`
```cpp
#ifndef TASKMANAGER_H
#define TASKMANAGER_H

#include <QList>
#include "Task.h"
#include "DatabaseManager.h"

class TaskManager {
public:
    TaskManager();
    ~TaskManager
