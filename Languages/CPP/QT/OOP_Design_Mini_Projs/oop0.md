
```
Cmake Configration for CLion
"-DCMAKE_PREFIX_PATH=C:\Qt\6.7.2\mingw_64"
```

Here's a simple Qt application with UI components created using the widgets class, following OOP principles, and separated into `.h` and `.cpp` files. The app will have a main window with a button, and we'll create a separate class for the button's styling.

### File Structure:
- `main.cpp`
- `MainWindow.h`
- `MainWindow.cpp`
- `ButtonStyler.h`
- `ButtonStyler.cpp`

### `main.cpp`
```cpp
#include <QApplication>
#include "MainWindow.h"

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    MainWindow window;
    window.show();
    return app.exec();
}
```

### `MainWindow.h`
```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QPushButton>
#include "ButtonStyler.h"

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    QPushButton *button;
    ButtonStyler *styler;
};

#endif // MAINWINDOW_H
```

### `MainWindow.cpp`
```cpp
#include "MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), button(new QPushButton("Click Me", this)), styler(new ButtonStyler()) {
    // Set button geometry
    button->setGeometry(50, 50, 200, 50);

    // Apply style to the button
    styler->applyStyle(button);
}

MainWindow::~MainWindow() {
    delete button;
    delete styler;
}
```

### `ButtonStyler.h`
```cpp
#ifndef BUTTONSTYLER_H
#define BUTTONSTYLER_H

#include <QPushButton>

class ButtonStyler {
public:
    ButtonStyler();
    void applyStyle(QPushButton *button);
};

#endif // BUTTONSTYLER_H
```

### `ButtonStyler.cpp`
```cpp
#include "ButtonStyler.h"

ButtonStyler::ButtonStyler() {
    // Constructor can be used to initialize styles or other resources if needed
}

void ButtonStyler::applyStyle(QPushButton *button) {
    // Apply a simple stylesheet to the button
    button->setStyleSheet("QPushButton { background-color: lightblue; border-radius: 10px; }");
}
```

### Explanation:
- **MainWindow**: The `MainWindow` class handles the main window logic and contains a button (`QPushButton`).
- **ButtonStyler**: The `ButtonStyler` class is responsible for styling the button. This class is separate from the main logic, demonstrating the separation of concerns in OOP.
- The UI components are created using the widgets class, not `.ui` files.

You can compile and run this Qt application in any Qt-compatible IDE like CLion or directly with `qmake`/`cmake`.
