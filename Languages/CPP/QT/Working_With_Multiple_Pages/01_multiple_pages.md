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
