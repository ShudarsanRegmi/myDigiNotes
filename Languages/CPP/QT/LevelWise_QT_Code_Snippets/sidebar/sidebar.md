

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

`mainwindow.h`

```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QStackedWidget>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
private:
    QStackedWidget *stackedWidget;  // Private member
    QWidget *createSidebar();  // Method to create sidebar layout


};
#endif // MAINWINDOW_H

```


`mainwindow.cpp`

```cpp
#include "mainwindow.h"
#include <QDebug>
#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
#include <QVBoxLayout>
#include <QWidget>
#include <QStackedWidget>
#include <QMenuBar>
#include <QAction>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    qDebug() << "Constructor called";

    // Create the central widget
    stackedWidget = new QStackedWidget;

    // Create pages (widgets) (commented out, but include these when ready)
    QWidget *homePage = new QWidget;
    QVBoxLayout *homeLayout = new QVBoxLayout;
    homeLayout->addWidget(new QPushButton("Welcome to Home Page"));
    homePage->setLayout(homeLayout);

    QWidget *settingsPage = new QWidget;
    QVBoxLayout *settingsLayout = new QVBoxLayout;
    settingsLayout->addWidget(new QPushButton("Settings Page"));
    settingsPage->setLayout(settingsLayout);

    QWidget *aboutPage = new QWidget;
    QVBoxLayout *aboutLayout = new QVBoxLayout;
    aboutLayout->addWidget(new QPushButton("About Page"));
    aboutPage->setLayout(aboutLayout);

    // Add pages to stackedWidget
    stackedWidget->addWidget(homePage);
    stackedWidget->addWidget(settingsPage);
    stackedWidget->addWidget(aboutPage);

    // Set the stacked widget as the central widget
    setCentralWidget(stackedWidget);

    // Create menu actions
    QAction *homeAction = new QAction("Home", this);
    QAction *settingsAction = new QAction("Settings", this);
    QAction *aboutAction = new QAction("About", this);

    // Create the menu bar
    QMenu *menu = menuBar()->addMenu("Navigate");
    menu->addAction(homeAction);
    menu->addAction(settingsAction);
    menu->addAction(aboutAction);

    // Connect actions to page switching
    connect(homeAction, &QAction::triggered, [=]() {
        stackedWidget->setCurrentIndex(0);
    });
    connect(settingsAction, &QAction::triggered, [=]() {
        stackedWidget->setCurrentIndex(1);
    });
    connect(aboutAction, &QAction::triggered, [=]() {
        stackedWidget->setCurrentIndex(2);
    });

    setWindowTitle("Minimal Classical App");
    resize(400, 300);

}

MainWindow::~MainWindow() {}



QWidget* MainWindow::createSidebar() {
    // Create a sidebar widget
    QWidget *sidebar = createSidebar();


    QVBoxLayout *sidebarLayout = new QVBoxLayout;

    // Create buttons for the sidebar
    QPushButton *homeButton = new QPushButton("Home");
    QPushButton *settingsButton = new QPushButton("Settings");
    QPushButton *aboutButton = new QPushButton("About");

    // Add buttons to the sidebar layout
    sidebarLayout->addWidget(homeButton);
    sidebarLayout->addWidget(settingsButton);
    sidebarLayout->addWidget(aboutButton);
    sidebarLayout->addStretch();  // Pushes buttons to the top

    // Connect the buttons to switch pages
    connect(homeButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(0);  // Switch to home page
    });
    connect(settingsButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(1);  // Switch to settings page
    });
    connect(aboutButton, &QPushButton::clicked, [=]() {
        stackedWidget->setCurrentIndex(2);  // Switch to about page
    });

    // Set the sidebar layout
    sidebar->setLayout(sidebarLayout);
    return sidebar;
}

```
