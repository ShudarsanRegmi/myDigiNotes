# Creating a simple UI without using .ui files in Qt creator

```cpp
#include "mainwindow.h"
#include <QVBoxLayout>
#include <QWidget>
#include <QPushButton>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    QWidget *centralWidget = new QWidget(this);
    this->setWindowTitle("Basic Application With Oru Push Button");
    setCentralWidget(centralWidget);

    QPushButton *btn1 = new QPushButton("Click Me");

    QVBoxLayout *layout = new QVBoxLayout(centralWidget);
    layout->addWidget(btn1);
    layout->addWidget(new QPushButton("Click..."));

}

MainWindow::~MainWindow() {}

```
### Output

![image](https://github.com/user-attachments/assets/d6f09201-5828-452b-8f9c-f081e5b469e2)

