# Sidebar

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

`mainwindow.cpp`

```cpp
#include "mainwindow.h"
#include <QHBoxLayout>
#include <QIcon>
#include <QLabel>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent) {
    // Create the main layout that will hold both the sidebar and the main content
    QWidget *centralWidget = new QWidget;
    QHBoxLayout *mainLayout = new QHBoxLayout;

    // Create the sidebar
    QWidget *sidebar = createSidebar();

    // Create the central widget (content area) using QStackedWidget
    stackedWidget = new QStackedWidget;

    // Create pages (widgets)
    QWidget *dashboardPage = new QWidget;
    QVBoxLayout *dashboardLayout = new QVBoxLayout;
    dashboardLayout->addWidget(new QLabel("Dashboard Page"));
    dashboardPage->setLayout(dashboardLayout);

    QWidget *studentsPage = new QWidget;
    QVBoxLayout *studentsLayout = new QVBoxLayout;
    studentsLayout->addWidget(new QLabel("Students Management Page"));
    studentsPage->setLayout(studentsLayout);

    QWidget *coursesPage = new QWidget;
    QVBoxLayout *coursesLayout = new QVBoxLayout;
    coursesLayout->addWidget(new QLabel("Courses Management Page"));
    coursesPage->setLayout(coursesLayout);

    QWidget *attendancePage = new QWidget;
    QVBoxLayout *attendanceLayout = new QVBoxLayout;
    attendanceLayout->addWidget(new QLabel("Attendance Page"));
    attendancePage->setLayout(attendanceLayout);

    QWidget *settingsPage = new QWidget;
    QVBoxLayout *settingsLayout = new QVBoxLayout;
    settingsLayout->addWidget(new QLabel("Settings Page"));
    settingsPage->setLayout(settingsLayout);

    // Add pages to stackedWidget
    stackedWidget->addWidget(dashboardPage);
    stackedWidget->addWidget(studentsPage);
    stackedWidget->addWidget(coursesPage);
    stackedWidget->addWidget(attendancePage);
    stackedWidget->addWidget(settingsPage);

    // Add sidebar and central widget to the main layout
    mainLayout->addWidget(sidebar);         // Sidebar on the left
    mainLayout->addWidget(stackedWidget);   // Central content area

    // Set the layout for the central widget
    centralWidget->setLayout(mainLayout);
    setCentralWidget(centralWidget);

    setWindowTitle("Student Management System");
    resize(800, 600);
}

MainWindow::~MainWindow() {
    // Destructor implementation (if needed)
}

QWidget* MainWindow::createSidebar() {
    // Create a sidebar widget
    QWidget *sidebar = new QWidget;
    QVBoxLayout *sidebarLayout = new QVBoxLayout;

    // Create buttons for the sidebar with icons
    QPushButton *dashboardButton = new QPushButton("Dashboard");
    dashboardButton->setIcon(QIcon(":/icons/dashboard.png"));

    QPushButton *studentsButton = new QPushButton("Students");
    studentsButton->setIcon(QIcon(":/icons/students.png"));

    QPushButton *coursesButton = new QPushButton("Courses");
    coursesButton->setIcon(QIcon(":/icons/courses.png"));

    QPushButton *attendanceButton = new QPushButton("Attendance");
    attendanceButton->setIcon(QIcon(":/icons/attendance.png"));

    QPushButton *settingsButton = new QPushButton("Settings");
    settingsButton->setIcon(QIcon(":/icons/settings.png"));

    // Style the sidebar
    sidebarLayout->addWidget(dashboardButton);
    sidebarLayout->addWidget(studentsButton);
    sidebarLayout->addWidget(coursesButton);
    sidebarLayout->addWidget(attendanceButton);
    sidebarLayout->addWidget(settingsButton);
    sidebarLayout->addStretch();  // Pushes buttons to the top
    sidebar->setLayout(sidebarLayout);

    // Set a stylesheet to customize the sidebar
    sidebar->setStyleSheet(
        "QWidget {"
        "  background-color: #2C3E50;"
        "  padding: 10px;"
        "}"
        "QPushButton {"
        "  color: white;"
        "  background-color: #34495E;"
        "  padding: 10px;"
        "  border: none;"
        "  text-align: left;"
        "  font-size: 16px;"
        "  margin-bottom: 5px;"
        "}"
        "QPushButton:hover {"
        "  background-color: #1ABC9C;"
        "}"
        );

    // Connect the buttons to switch pages in the stackedWidget
    connect(dashboardButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(0);  // Switch to dashboard page
    });
    connect(studentsButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(1);  // Switch to students page
    });
    connect(coursesButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(2);  // Switch to courses page
    });
    connect(attendanceButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(3);  // Switch to attendance page
    });
    connect(settingsButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(4);  // Switch to settings page
    });

    return sidebar;
}

```

`mainwindow.h`

```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QStackedWidget>
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    QStackedWidget *stackedWidget;
    QWidget *createSidebar();  // Method to create the sidebar
};
#endif // MAINWINDOW_H

```

## Output

![image](https://github.com/user-attachments/assets/0657a040-e014-4fce-80b2-e2b8f5ac1e6f)

