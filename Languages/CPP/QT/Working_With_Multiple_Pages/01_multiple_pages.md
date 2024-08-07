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

## 03 - Implementing `prevous page` and `next page` feture

### Implementation 1: With simple logic (but not scalable)
> Define slots for each button, get the current index and set the index to current index + 1 under mod total pages. Do this for each buttons

**Step 1: Define slots in mainwindow.h**

```cpp
// mainwindow.h
private slots:
    void on_pg1_prev_clicked();
    void on_pg2_prev_clicked();
    void on_pg3_prev_clicked();
```

**Step 2: Write slots for each buttons**

```cpp
mainwindow.cpp
void MainWindow::on_pg1_prev_clicked()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index-1+total_widgets)%total_widgets);
}

void MainWindow::on_pg2_prev_clicked()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index-1+total_widgets)%total_widgets);
}


void MainWindow::on_pg3_prev_clicked()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index-1+total_widgets)%total_widgets);
}

```
### Implementation 2: With scalable logic
> Define one slot and connect each buttons to that slot. the slot will get the current index and set it to current index + 1 under modulo total pages

**Step 1: Define slots in mainwindow.h**

```cpp
// mainwindow.h
private slots:
    void navigate_next();
```

**Step 2: Write slots for each buttons**

```cpp
mainwindow.cpp
void MainWindow::navigate_next()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index+1)%total_widgets);
}
```

**Step 3: Connect each slots to click signals**

```cpp
    connect(ui->pg1_next, &QPushButton::clicked, this, &MainWindow::navigateNext);
    connect(ui->pg2_next, &QPushButton::clicked, this, &MainWindow::navigateNext);
    connect(ui->pg3_next, &QPushButton::clicked, this, &MainWindow::navigateNext);
```

### The overall code  for above two implemntation

```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QVBoxLayout>
#include <QPushButton>
#include <QLabel>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->pg1_next, &QPushButton::clicked, this, &MainWindow::navigateNext);
    connect(ui->pg2_next, &QPushButton::clicked, this, &MainWindow::navigateNext);
    connect(ui->pg3_next, &QPushButton::clicked, this, &MainWindow::navigateNext);

}

MainWindow::~MainWindow()
{
    delete ui;
}

// Level 1 Logic to implement previous next feature
/*
create slot for eacch previous buttons and for each buttons
When the button is pressed
get the current index
set the current index to current index under modulo total pages...
*/

void MainWindow::on_pg1_prev_clicked()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index-1+total_widgets)%total_widgets);

}

void MainWindow::on_pg2_prev_clicked()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index-1+total_widgets)%total_widgets);
}


void MainWindow::on_pg3_prev_clicked()
{
    int cur_index = ui->stackedWidget->currentIndex();
    int total_widgets = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index-1+total_widgets)%total_widgets);
}

/*
Level: 2
Define Only one slot to handle nagivation to next and previous
Here we'll show by previous navigation
*/


void MainWindow::navigateNext() {
    int cur_index = ui->stackedWidget->currentIndex();
    int total_pages = ui->stackedWidget->count();
    ui->stackedWidget->setCurrentIndex((cur_index+1)%total_pages);
}

```
