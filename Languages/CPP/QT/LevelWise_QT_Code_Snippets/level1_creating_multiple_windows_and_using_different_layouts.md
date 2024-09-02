# Creating Multiple windows and using different layouts

# Code
`mainwindow.cpp`

```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QPushButton>
#include <QVBoxLayout>
#include <QString>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow) // this is for
{
    ui->setupUi(this); // this is for setting up the ui created from .ui files

    QWidget *window = new QWidget;
    window->setWindowTitle("title");

    QWidget *centralWidget = new QWidget(this);
    setCentralWidget(centralWidget);



    QVBoxLayout *layout = new QVBoxLayout(centralWidget);

    QPushButton *btn0 = new QPushButton("Click Me 1");
    QPushButton *btn1 = new QPushButton("Click Me 2");
    QPushButton *btn2 = new QPushButton("Click Me 3");



    layout->addWidget(btn0);
    layout->addWidget(btn1);
    layout->addWidget(btn2);

    QHBoxLayout *lay2 = new QHBoxLayout(window);

    QPushButton *btn3 = new QPushButton("Click Me 1");
    QPushButton *btn4 = new QPushButton("Click Me 2");
    QPushButton *btn5 = new QPushButton("Click Me 3");

    lay2->addWidget(btn3);
    lay2->addWidget(btn4);
    lay2->addWidget(btn5);



    window->show();
    centralWidget->show();

}

MainWindow::~MainWindow()
{
    delete ui;
}

```

## Output
![image](https://github.com/user-attachments/assets/b6f89a8a-f657-4bbd-a08b-cbd9f05960b1)
