# Some important general points about  Qt

- In GUI programming, when we change one widget, we often want another widget to be notified. More generally, we want objects of any kind to be able to communicate with one another. For example, if a user clicks a Close button, we probably want the window's close() function to be called.


### Creating a layout and adding widget to it

```cpp
  QVBoxLayout *layout = new QVBoxLayout;
  layout->addWidget(pageComboBox);
  layout->addWidget(stackedWidget);
```

### Creating a central widget
```cpp
    QWidget *centralWidget = new QWidget;
    centralWidget->setLayout(layout);
    setCentralWidget(centralWidget);
```
