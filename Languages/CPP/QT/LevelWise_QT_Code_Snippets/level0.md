# Level - 0

## Theories
- QApplication Object
- main function and passing argc and argv to Qapplication
- Creating a simple Qt Widget

For any GUI application using Qt, there is precisely one QApplication object, no matter whether the application has 0, 1, 2 or more windows at any given time. For non-QWidget based Qt applications, use QGuiApplication instead, as it does not depend on the QtWidgets library.

## HelloWorld Program (using QLabel Widget)
```cpp
#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    QLabel *label = new QLabel(nullptr);
    label->setText("Hello, World");
    label->show();
    
    return QApplication::exec();
}
```

## Output

## Explanation
- .show() method makes the widget visible

![image](https://github.com/user-attachments/assets/8f40a638-3ac3-4e12-a64b-6d91d3690355)

## Creating Multiple Widgets
```cpp
#include <QApplication>
#include <QLabel>
#include <QPushButton>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    QLabel *label = new QLabel(nullptr);
    label->setText("Hello, World");
    label->show();

    QPushButton *button = new QPushButton(nullptr);
    button->setText("Click Me");
    button->show();

    return QApplication::exec();
}
```

## Output
![image](https://github.com/user-attachments/assets/50a50048-2e8b-4e07-b3c3-5a3c9cc47f35)

- Two separate window will be created. So we need to choose a layout
- Layouts in Qt automatically arrange and manage the size and position of child widgets within a parent widget. When a parent widget with a layout is shown, all its child widgets are automatically made visible and arranged according to the layout’s rules. 

**In summary**: Only the parent widget needs to call the `show()` method to make itself and its child widgets visible. 
