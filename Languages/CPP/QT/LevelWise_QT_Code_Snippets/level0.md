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


## Task-1 : Making a Live text edit and display along with clear button (without using any layout)

```cpp
#include <QApplication>
#include <QLineEdit>
#include <QLabel>
#include <QPushButton>
#include <QObject>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);

    QLineEdit *le = new QLineEdit();
    QLabel *l = new QLabel();
    QPushButton *btn = new QPushButton();
    btn->setText("Clear");

    QObject::connect(le, &QLineEdit::textChanged, [=]() {
        l->setText(le->text());
    });

    QObject::connect(btn, &QPushButton::clicked, [=]() {
        l->setText("");
        le->clear();
    });

    le->show();
    l->show();
    btn->show();

    return QApplication::exec();
}

```
## Output

![image](https://github.com/user-attachments/assets/9d1e3b4c-74cf-42be-b1c4-367bf3d89c71)

## Task - 2: Task - 1 with QVBoxLayout

```cpp
#include <QApplication>
#include <QLineEdit>
#include <QLabel>
#include <QPushButton>
#include <QObject>
#include <QVBoxLayout>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    QVBoxLayout *layout = new QVBoxLayout();

    QWidget window;

    QLineEdit *le = new QLineEdit();
    QLabel *l = new QLabel();
    QPushButton *btn = new QPushButton();
    btn->setText("Clear");

    QObject::connect(le, &QLineEdit::textChanged, [=]() {
        l->setText(le->text());
    });

    QObject::connect(btn, &QPushButton::clicked, [=]() {
        l->setText("");
        le->clear();
    });

    layout->addWidget(le);
    layout->addWidget(btn);
    layout->addWidget(l);

    window.setLayout(layout);

    window.show();
    
    return QApplication::exec();
}
```
## Output

![image](https://github.com/user-attachments/assets/2803f9d7-1460-4d00-93ac-dadcbe9e5feb)

## Task - 3 : Task - 1 with QHBoxLayout

```cpp
    #include <QApplication>
    #include <QLineEdit>
    #include <QLabel>
    #include <QPushButton>
    #include <QObject>
    #include <QHboxLayout>

    int main(int argc, char *argv[]) {
        QApplication a(argc, argv);
        QHBoxLayout *layout = new QHBoxLayout();

        QWidget window;

        QLineEdit *le = new QLineEdit();
        QLabel *l = new QLabel();
        QPushButton *btn = new QPushButton();
        btn->setText("Clear");

        QObject::connect(le, &QLineEdit::textChanged, [=]() {
            l->setText(le->text());
        });

        QObject::connect(btn, &QPushButton::clicked, [=]() {
            l->setText("");
            le->clear();
        });

        layout->addWidget(le);
        layout->addWidget(btn);
        layout->addWidget(l);

        window.setLayout(layout);

        window.show();

        return QApplication::exec();
    }

```

## Output

![image](https://github.com/user-attachments/assets/b6368c87-7af5-4947-ad86-38cb4ae62ba8)
