# This is a TaskManger app with OOP Design

I completely understand! Let’s move away from those basic inheritance examples and build a simple, practical Qt app using real OOP principles.

We’ll make a **"Task Manager"** app, where you can add tasks, view them in a list, and mark them as completed. It will be structured with proper OOP design to show how different classes interact and make the app modular and maintainable.

### Project Overview:
- **MainWindow**: Handles the main UI (menu bar, buttons, etc.)
- **TaskManager**: Manages the collection of tasks (add, delete, mark complete)
- **Task**: Represents an individual task (description, status)
- **TaskWidget**: Displays individual tasks in the UI (inherits `QWidget`)

---

### Step 1: Set Up Your Project Structure

Create a Qt project. You’ll have the following files:
```
TaskManagerApp/
├── main.cpp
├── mainwindow.h
├── mainwindow.cpp
├── taskmanager.h
├── taskmanager.cpp
├── task.h
├── task.cpp
├── taskwidget.h
├── taskwidget.cpp
├── mainwindow.ui
└── taskwidget.ui
```

### Step 2: Define the Classes

#### **Task Class (`task.h` / `task.cpp`)**

This class represents individual tasks.

```cpp
// task.h
#ifndef TASK_H
#define TASK_H

#include <QString>

class Task {
public:
    Task(const QString& description);

    QString getDescription() const;
    bool isCompleted() const;

    void setDescription(const QString& description);
    void setCompleted(bool completed);

private:
    QString description;
    bool completed;
};

#endif // TASK_H
```

```cpp
// task.cpp
#include "task.h"

Task::Task(const QString& description) : description(description), completed(false) {}

QString Task::getDescription() const {
    return description;
}

bool Task::isCompleted() const {
    return completed;
}

void Task::setDescription(const QString& description) {
    this->description = description;
}

void Task::setCompleted(bool completed) {
    this->completed = completed;
}
```

#### **TaskManager Class (`taskmanager.h` / `taskmanager.cpp`)**

This class handles the logic for managing tasks, like adding and removing them.

```cpp
// taskmanager.h
#ifndef TASKMANAGER_H
#define TASKMANAGER_H

#include <QVector>
#include "task.h"

class TaskManager {
public:
    void addTask(const QString& description);
    void removeTask(int index);
    void completeTask(int index);

    QVector<Task*> getTasks() const;

private:
    QVector<Task*> tasks;
};

#endif // TASKMANAGER_H
```

```cpp
// taskmanager.cpp
#include "taskmanager.h"

void TaskManager::addTask(const QString& description) {
    tasks.append(new Task(description));
}

void TaskManager::removeTask(int index) {
    if (index >= 0 && index < tasks.size()) {
        delete tasks[index];
        tasks.removeAt(index);
    }
}

void TaskManager::completeTask(int index) {
    if (index >= 0 && index < tasks.size()) {
        tasks[index]->setCompleted(true);
    }
}

QVector<Task*> TaskManager::getTasks() const {
    return tasks;
}
```

#### **TaskWidget Class (`taskwidget.h` / `taskwidget.cpp`)**

This class represents the UI component for each task.

```cpp
// taskwidget.h
#ifndef TASKWIDGET_H
#define TASKWIDGET_H

#include <QWidget>
#include "task.h"

namespace Ui {
class TaskWidget;
}

class TaskWidget : public QWidget {
    Q_OBJECT

public:
    explicit TaskWidget(Task* task, QWidget *parent = nullptr);
    ~TaskWidget();

private slots:
    void on_checkBox_toggled(bool checked);

private:
    Ui::TaskWidget *ui;
    Task* task;
};

#endif // TASKWIDGET_H
```

```cpp
// taskwidget.cpp
#include "taskwidget.h"
#include "ui_taskwidget.h"

TaskWidget::TaskWidget(Task* task, QWidget *parent) :
    QWidget(parent),
    ui(new Ui::TaskWidget),
    task(task)
{
    ui->setupUi(this);
    ui->label->setText(task->getDescription());
    ui->checkBox->setChecked(task->isCompleted());
}

TaskWidget::~TaskWidget() {
    delete ui;
}

void TaskWidget::on_checkBox_toggled(bool checked) {
    task->setCompleted(checked);
}
```

#### **MainWindow (`mainwindow.h` / `mainwindow.cpp`)**

The main window handles the overall UI and interaction between components.

```cpp
// mainwindow.h
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "taskmanager.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_addTaskButton_clicked();

private:
    Ui::MainWindow *ui;
    TaskManager taskManager;

    void updateTaskList();
};

#endif // MAINWINDOW_H
```

```cpp
// mainwindow.cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "taskwidget.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::on_addTaskButton_clicked() {
    QString taskDescription = ui->taskInput->text();
    if (!taskDescription.isEmpty()) {
        taskManager.addTask(taskDescription);
        updateTaskList();
        ui->taskInput->clear();
    }
}

void MainWindow::updateTaskList() {
    // Clear the current list
    QLayoutItem* child;
    while ((child = ui->taskListLayout->takeAt(0)) != nullptr) {
        delete child->widget();
        delete child;
    }

    // Add all tasks to the UI
    for (Task* task : taskManager.getTasks()) {
        TaskWidget* taskWidget = new TaskWidget(task);
        ui->taskListLayout->addWidget(taskWidget);
    }
}
```

### Step 3: UI Design (`mainwindow.ui` and `taskwidget.ui`)

- **`mainwindow.ui`** should have a `QLineEdit` for inputting tasks, a `QPushButton` to add tasks, and a `QVBoxLayout` to hold the tasks.
- **`taskwidget.ui`** should have a `QCheckBox` to mark tasks as completed and a `QLabel` to display the task description.

### Step 4: Main Entry (`main.cpp`)

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

---

### Explanation

- **Task Manager** manages the logic of the application. It adds and deletes tasks and tracks their completion status.
- **MainWindow** serves as the controller, handling user input and updating the UI.
- **Task** represents the core data model. This separation of concerns makes it easier to manage and scale your application.
- **TaskWidget** is responsible for representing individual tasks in the UI, and each task interacts with the core logic via the `Task` class.

This structure demonstrates how OOP principles like **encapsulation**, **abstraction**, and **separation of concerns** are used in a real Qt project, making your code modular, reusable, and maintainable.

This simple app can be extended further by adding features like persistence (saving tasks to a file or database) or more complex task management logic.
