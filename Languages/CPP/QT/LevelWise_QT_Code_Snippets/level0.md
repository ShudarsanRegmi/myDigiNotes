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

## Task - 4: DashBoard interface

```cpp
#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QComboBox>
#include <QCheckBox>
#include <QProgressBar>
#include <QTextEdit>
#include <QGroupBox>
#include <QTimer>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Create main window
    QWidget window;
    window.setWindowTitle("Dashboard Interface");

    // === User Information Panel ===
    QLabel *nameLabel = new QLabel("Name:");
    QLineEdit *nameEdit = new QLineEdit();

    QLabel *roleLabel = new QLabel("Role:");
    QComboBox *roleCombo = new QComboBox();
    roleCombo->addItems({"Admin", "User", "Guest"});

    QLabel *statusLabel = new QLabel("Status:");
    QCheckBox *onlineStatus = new QCheckBox("Online");

    QHBoxLayout *userInfoLayout = new QHBoxLayout();
    userInfoLayout->addWidget(nameLabel);
    userInfoLayout->addWidget(nameEdit);
    userInfoLayout->addWidget(roleLabel);
    userInfoLayout->addWidget(roleCombo);
    userInfoLayout->addWidget(statusLabel);
    userInfoLayout->addWidget(onlineStatus);

    QGroupBox *userInfoGroup = new QGroupBox("User Information");
    userInfoGroup->setLayout(userInfoLayout);

    // === Control Buttons Panel ===
    QPushButton *startButton = new QPushButton("Start");
    QPushButton *stopButton = new QPushButton("Stop");
    QPushButton *resetButton = new QPushButton("Reset");

    QHBoxLayout *controlButtonLayout = new QHBoxLayout();
    controlButtonLayout->addWidget(startButton);
    controlButtonLayout->addWidget(stopButton);
    controlButtonLayout->addWidget(resetButton);

    QGroupBox *controlButtonGroup = new QGroupBox("Control Panel");
    controlButtonGroup->setLayout(controlButtonLayout);

    // === Settings Panel ===
    QLabel *brightnessLabel = new QLabel("Brightness:");
    QSlider *brightnessSlider = new QSlider(Qt::Horizontal);
    brightnessSlider->setRange(0, 100);
    brightnessSlider->setValue(50);

    QLabel *volumeLabel = new QLabel("Volume:");
    QSlider *volumeSlider = new QSlider(Qt::Horizontal);
    volumeSlider->setRange(0, 100);
    volumeSlider->setValue(75);

    QVBoxLayout *settingsLayout = new QVBoxLayout();
    settingsLayout->addWidget(brightnessLabel);
    settingsLayout->addWidget(brightnessSlider);
    settingsLayout->addWidget(volumeLabel);
    settingsLayout->addWidget(volumeSlider);

    QGroupBox *settingsGroup = new QGroupBox("Settings");
    settingsGroup->setLayout(settingsLayout);

    // === Status & Notifications Panel ===
    QProgressBar *progressBar = new QProgressBar();
    progressBar->setRange(0, 100);
    progressBar->setValue(0);

    QTextEdit *notifications = new QTextEdit();
    notifications->setReadOnly(true);
    notifications->setText("Notifications:\n");

    QVBoxLayout *statusLayout = new QVBoxLayout();
    statusLayout->addWidget(progressBar);
    statusLayout->addWidget(notifications);

    QGroupBox *statusGroup = new QGroupBox("Status & Notifications");
    statusGroup->setLayout(statusLayout);

    // === Main Layout ===
    QVBoxLayout *leftLayout = new QVBoxLayout();
    leftLayout->addWidget(userInfoGroup);
    leftLayout->addWidget(controlButtonGroup);
    leftLayout->addWidget(settingsGroup);

    QVBoxLayout *rightLayout = new QVBoxLayout();
    rightLayout->addWidget(statusGroup);

    QHBoxLayout *mainLayout = new QHBoxLayout();
    mainLayout->addLayout(leftLayout, 2);  // Left panel with 2 parts width
    mainLayout->addLayout(rightLayout, 1); // Right panel with 1 part width

    window.setLayout(mainLayout);

    // === Functionality ===
    QTimer *progressTimer = new QTimer(&window);

    // Start button functionality
    QObject::connect(startButton, &QPushButton::clicked, [&]() {
        notifications->append("Process started...");
        progressTimer->start(100);
    });

    // Stop button functionality
    QObject::connect(stopButton, &QPushButton::clicked, [&]() {
        notifications->append("Process stopped.");
        progressTimer->stop();
    });

    // Reset button functionality
    QObject::connect(resetButton, &QPushButton::clicked, [&]() {
        notifications->append("Progress reset.");
        progressBar->setValue(0);
        progressTimer->stop();
    });

    // Progress bar update simulation
    QObject::connect(progressTimer, &QTimer::timeout, [&]() {
        int progress = progressBar->value();
        if (progress < 100) {
            progressBar->setValue(progress + 5);
        } else {
            notifications->append("Process completed!");
            progressTimer->stop();
        }
    });

    // Show the main window
    window.show();

    return app.exec();
}
```
## Output
![image](https://github.com/user-attachments/assets/e906b1f6-bdf3-4240-a672-9636af0c4efc)
