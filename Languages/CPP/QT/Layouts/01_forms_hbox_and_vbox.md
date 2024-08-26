# Examples code to show the use of QHBoxLayout and QVBoxLayout

```cpp
#include <QApplication>
#include <QWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QMessageBox>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Create main window
    QWidget window;
    window.setWindowTitle("User Form");

    // Create widgets
    QLabel *nameLabel = new QLabel("Name:");
    QLineEdit *nameEdit = new QLineEdit();

    QLabel *ageLabel = new QLabel("Age:");
    QLineEdit *ageEdit = new QLineEdit();

    QLabel *emailLabel = new QLabel("Email:");
    QLineEdit *emailEdit = new QLineEdit();

    QPushButton *submitButton = new QPushButton("Submit");
    QPushButton *clearButton = new QPushButton("Clear");

    QLabel *outputLabel = new QLabel();

    // Horizontal Layout for form inputs
    QHBoxLayout *nameLayout = new QHBoxLayout();
    nameLayout->addWidget(nameLabel);
    nameLayout->addWidget(nameEdit);

    QHBoxLayout *ageLayout = new QHBoxLayout();
    ageLayout->addWidget(ageLabel);
    ageLayout->addWidget(ageEdit);

    QHBoxLayout *emailLayout = new QHBoxLayout();
    emailLayout->addWidget(emailLabel);
    emailLayout->addWidget(emailEdit);

    // Horizontal Layout for buttons
    QHBoxLayout *buttonLayout = new QHBoxLayout();
    buttonLayout->addWidget(submitButton);
    buttonLayout->addWidget(clearButton);

    // Main vertical layout to arrange everything
    QVBoxLayout *mainLayout = new QVBoxLayout();
    mainLayout->addLayout(nameLayout);
    mainLayout->addLayout(ageLayout);
    mainLayout->addLayout(emailLayout);
    mainLayout->addLayout(buttonLayout);
    mainLayout->addWidget(outputLabel);

    // Set layout for the main window
    window.setLayout(mainLayout);

    // Connect button functionality
    QObject::connect(submitButton, &QPushButton::clicked, [&]() {
        QString name = nameEdit->text();
        QString age = ageEdit->text();
        QString email = emailEdit->text();

        if (name.isEmpty() || age.isEmpty() || email.isEmpty()) {
            QMessageBox::warning(&window, "Input Error", "Please fill in all fields!");
        } else {
            outputLabel->setText("Submitted Info: " + name + ", " + age + " years old, " + email);
        }
    });

    QObject::connect(clearButton, &QPushButton::clicked, [&]() {
        nameEdit->clear();
        ageEdit->clear();
        emailEdit->clear();
        outputLabel->clear();
    });

    // Show the main window
    window.show();

    return app.exec();
}

```
## Output

![image](https://github.com/user-attachments/assets/4031869e-c86c-4896-8d2f-cba4b0bb0ea9)

## Media - Player app design

```cpp
#include <QApplication>
#include <QWidget>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QPushButton>
#include <QSlider>
#include <QLabel>
#include <QMessageBox>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Create main window
    QWidget window;
    window.setWindowTitle("Media Player Control");

    // Create buttons for media control
    QPushButton *playButton = new QPushButton("Play");
    QPushButton *pauseButton = new QPushButton("Pause");
    QPushButton *stopButton = new QPushButton("Stop");
    QPushButton *prevButton = new QPushButton("Previous");
    QPushButton *nextButton = new QPushButton("Next");

    // Create a slider for volume control
    QSlider *volumeSlider = new QSlider(Qt::Horizontal);
    volumeSlider->setRange(0, 100);
    volumeSlider->setValue(50);  // Default volume level

    QLabel *volumeLabel = new QLabel("Volume: 50%");

    // Horizontal layout for media control buttons
    QHBoxLayout *controlLayout = new QHBoxLayout();
    controlLayout->addWidget(prevButton);
    controlLayout->addWidget(playButton);
    controlLayout->addWidget(pauseButton);
    controlLayout->addWidget(stopButton);
    controlLayout->addWidget(nextButton);

    // Horizontal layout for volume control
    QHBoxLayout *volumeLayout = new QHBoxLayout();
    volumeLayout->addWidget(new QLabel("Volume:"));
    volumeLayout->addWidget(volumeSlider);
    volumeLayout->addWidget(volumeLabel);

    // Main vertical layout to arrange everything
    QVBoxLayout *mainLayout = new QVBoxLayout();
    mainLayout->addLayout(controlLayout);   // Add media control buttons layout
    mainLayout->addLayout(volumeLayout);    // Add volume slider layout

    // Set layout for the main window
    window.setLayout(mainLayout);

    // Dummy button functionality
    QObject::connect(playButton, &QPushButton::clicked, [&]() {
        QMessageBox::information(&window, "Media Player", "Playing media...");
    });

    QObject::connect(pauseButton, &QPushButton::clicked, [&]() {
        QMessageBox::information(&window, "Media Player", "Pausing media...");
    });

    QObject::connect(stopButton, &QPushButton::clicked, [&]() {
        QMessageBox::information(&window, "Media Player", "Stopping media...");
    });

    QObject::connect(prevButton, &QPushButton::clicked, [&]() {
        QMessageBox::information(&window, "Media Player", "Playing previous track...");
    });

    QObject::connect(nextButton, &QPushButton::clicked, [&]() {
        QMessageBox::information(&window, "Media Player", "Playing next track...");
    });

    // Volume slider functionality
    QObject::connect(volumeSlider, &QSlider::valueChanged, [&]() {
        int volume = volumeSlider->value();
        volumeLabel->setText("Volume: " + QString::number(volume) + "%");
    });

    // Show the main window
    window.show();

    return app.exec();
}

```

## Output
![image](https://github.com/user-attachments/assets/615dbe51-d07e-4c03-a797-760347fbef8a)


## Dashboard app design
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
![image](https://github.com/user-attachments/assets/48a24f8b-c3d3-45ad-8a1c-2016b87177e3)
