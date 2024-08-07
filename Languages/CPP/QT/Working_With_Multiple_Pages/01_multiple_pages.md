## 01- Using QComboxBox(select widget) to chhose the page number and upating the page accordingly 

![image](https://github.com/user-attachments/assets/2265c42b-2028-44e6-a927-a59d852f4792)

```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QStackedWidget>
#include <QVBoxLayout>
#include <QComboBox>
#include <QLabel>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Create widgets for each page
    QWidget *firstPageWidget = new QWidget;
    QWidget *secondPageWidget = new QWidget;
    QWidget *thirdPageWidget = new QWidget;

    // Add some content to the pages so they are visible
    firstPageWidget->setStyleSheet("background-color: red;");
    secondPageWidget->setStyleSheet("background-color: green;");
    thirdPageWidget->setStyleSheet("background-color: blue;");

    // Create and set up the stacked widget
    QStackedWidget *stackedWidget = new QStackedWidget;
    stackedWidget->addWidget(firstPageWidget);
    stackedWidget->addWidget(secondPageWidget);
    stackedWidget->addWidget(thirdPageWidget);

    // Create and set up the combo box
    QComboBox *pageComboBox = new QComboBox;
    pageComboBox->addItem(tr("Page 1"));
    pageComboBox->addItem(tr("Page 2"));
    pageComboBox->addItem(tr("Page 3"));

    // Connect the combo box to the stacked widget
    connect(pageComboBox, &QComboBox::activated,
            stackedWidget, &QStackedWidget::setCurrentIndex);

    // Create a layout and add the combo box and stacked widget to it
    QVBoxLayout *layout = new QVBoxLayout;
    layout->addWidget(pageComboBox);
    layout->addWidget(stackedWidget);

    // Create a central widget and set the layout
    QWidget *centralWidget = new QWidget;
    centralWidget->setLayout(layout);

    // Set the central widget of the main window
        setCentralWidget(centralWidget);
}

MainWindow::~MainWindow()
{
    delete ui;
}

```
## 02 - Creating two pages using QT QWidget directly from the code

![image](https://github.com/user-attachments/assets/79b8eda4-7ff3-44fd-9472-f00293e51775)

```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    stackedWidget = new QStackedWidget(this);
    setCentralWidget(stackedWidget);

    page1 = new QWidget();
    page2 = new QWidget();

    QVBoxLayout *layout1 = new QVBoxLayout(page1);
    QVBoxLayout *layout2 = new QVBoxLayout(page2);

    // Buttons to switch pages
    QPushButton *button1 = new QPushButton("Go to page1", page1);
    QPushButton *button2 = new QPushButton("Go to page2", page2);


    QLabel *label1 = new QLabel("This is page 1", page1);
    QLabel *label2 = new QLabel("This is page 2", page2);

    layout1->addWidget(label1);
    layout2->addWidget(label2);

    connect(button1, &QPushButton::clicked, this, &MainWindow::switchToPage1);
    connect(button2, &QPushButton::clicked, this, &MainWindow::switchToPage2);

    layout1->addWidget(button1);
    layout1->addWidget(button2);

    layout2->addWidget(button1);
    layout2->addWidget(button1);

    stackedWidget->addWidget(page1);
    stackedWidget->addWidget(page2);


}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::switchToPage1() {
    stackedWidget->setCurrentWidget(page1);
}

void MainWindow::switchToPage2() {
    stackedWidget->setCurrentWidget(page2);
}

```

## 03 - 
