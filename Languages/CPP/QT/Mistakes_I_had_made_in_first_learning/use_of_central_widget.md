# Use of central Widget while setting up layouts in QMainWindow

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


    QVBoxLayout *layout = new QVBoxLayout(this);

    QPushButton *btn0 = new QPushButton("Click Me 1");
    QPushButton *btn1 = new QPushButton("Click Me 2");
    QPushButton *btn2 = new QPushButton("Click Me 3");
    QPushButton *btn3 = new QPushButton ("Click me 4");

    layout->addWidget(btn0);
    layout->addWidget(btn1);
    layout->addWidget(btn2);



    window->show();





}

MainWindow::~MainWindow()
{
    delete ui;
}

I want to add QVBoxyLaout in the mainwindow.
for that I'm passing this as argument to QVBoxLayout?
how to do it correctly?
