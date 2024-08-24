# Level - 0

## Theories
- QApplication Object
- main function and passing argc and argv to Qapplication
- Creating a simple Qt Widget

For any GUI application using Qt, there is precisely one QApplication object, no matter whether the application has 0, 1, 2 or more windows at any given time. For non-QWidget based Qt applications, use QGuiApplication instead, as it does not depend on the QtWidgets library.
