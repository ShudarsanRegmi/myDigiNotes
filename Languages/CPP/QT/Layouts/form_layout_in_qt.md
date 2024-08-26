# FormLayout in QT

```cpp
#include <QApplication>
#include <QWidget>
#include <QFormLayout>
#include <QLineEdit>
#include <QLabel>
#include <QPushButton>
#include <QComboBox>
#include <QSpinBox>
#include <QCheckBox>
#include <QRadioButton>
#include <QDateEdit>
#include <QTimeEdit>
#include <QDoubleSpinBox>
#include <QTextEdit>

class ComprehensiveForm : public QWidget {
public:
    ComprehensiveForm(QWidget *parent = nullptr) : QWidget(parent) {
        // Create widgets
        QLabel *nameLabel = new QLabel("Full Name:");
        QLineEdit *nameEdit = new QLineEdit();

        QLabel *emailLabel = new QLabel("Email Address:");
        QLineEdit *emailEdit = new QLineEdit();

        QLabel *ageLabel = new QLabel("Age:");
        QSpinBox *ageSpin = new QSpinBox();
        ageSpin->setRange(0, 120);

        QLabel *heightLabel = new QLabel("Height (cm):");
        QDoubleSpinBox *heightSpin = new QDoubleSpinBox();
        heightSpin->setRange(0.0, 300.0);

        QLabel *genderLabel = new QLabel("Gender:");
        QComboBox *genderCombo = new QComboBox();
        genderCombo->addItems({"Male", "Female", "Other"});

        QLabel *newsletterLabel = new QLabel("Subscribe to Newsletter:");
        QCheckBox *newsletterCheck = new QCheckBox();

        QLabel *dobLabel = new QLabel("Date of Birth:");
        QDateEdit *dobEdit = new QDateEdit();
        dobEdit->setCalendarPopup(true);

        QLabel *appointmentTimeLabel = new QLabel("Appointment Time:");
        QTimeEdit *appointmentTimeEdit = new QTimeEdit();

        QLabel *bioLabel = new QLabel("Bio:");
        QTextEdit *bioEdit = new QTextEdit();

        QLabel *favoriteColorLabel = new QLabel("Favorite Color:");
        QComboBox *favoriteColorCombo = new QComboBox();
        favoriteColorCombo->addItems({"Red", "Blue", "Green", "Yellow", "Other"});

        QLabel *statusLabel = new QLabel("Status:");
        QRadioButton *activeRadio = new QRadioButton("Active");
        QRadioButton *inactiveRadio = new QRadioButton("Inactive");

        QPushButton *submitButton = new QPushButton("Submit");

        // Create a QFormLayout
        QFormLayout *formLayout = new QFormLayout;

        // Add widgets to the form layout
        formLayout->addRow(nameLabel, nameEdit);
        formLayout->addRow(emailLabel, emailEdit);
        formLayout->addRow(ageLabel, ageSpin);
        formLayout->addRow(heightLabel, heightSpin);
        formLayout->addRow(genderLabel, genderCombo);
        formLayout->addRow(newsletterLabel, newsletterCheck);
        formLayout->addRow(dobLabel, dobEdit);
        formLayout->addRow(appointmentTimeLabel, appointmentTimeEdit);
        formLayout->addRow(bioLabel, bioEdit);
        formLayout->addRow(favoriteColorLabel, favoriteColorCombo);
        formLayout->addRow(statusLabel, activeRadio);
        formLayout->addRow("", inactiveRadio); // Add empty label for alignment

        // Add the submit button
        formLayout->addRow(submitButton);

        // Set the layout for the widget
        setLayout(formLayout);

        // Set window properties
        setWindowTitle("Comprehensive Form Layout Example");
        resize(400, 600);
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    ComprehensiveForm window;
    window.show();

    return app.exec();
}
  
```

## Output

![image](https://github.com/user-attachments/assets/d7fb4c0d-b480-46b2-a0b2-1eeeaa01dace)

## Form Layout in QT: A capstone form

```cpp
#include <QApplication>
#include <QFormLayout>
#include <QWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QRadioButton>
#include <QCheckBox>
#include <QComboBox>
#include <QSpinBox>
#include <QDoubleSpinBox>
#include <QSlider>
#include <QProgressBar>
#include <QTextEdit>
#include <QListWidget>
#include <QDateEdit>
#include <QTimeEdit>
#include <QDateTimeEdit>
#include <QDial>
#include <QLabel>
#include <QScrollBar>
#include <QGroupBox>
#include <QTabWidget>
#include <QHBoxLayout>

class CapstoneForm : public QWidget {
public:
    CapstoneForm(QWidget *parent = nullptr) : QWidget(parent) {
        // Create form layout
        QFormLayout *formLayout = new QFormLayout(this);

        // Add Components to the Form Layout
        formLayout->addRow("Line Edit:", new QLineEdit(this));
        formLayout->addRow("Password:", new QLineEdit(this));

        formLayout->addRow("Combo Box:", createComboBox());
        formLayout->addRow("List Widget:", createListWidget());
        formLayout->addRow("Radio Button 1:", new QRadioButton("Option 1", this));
        formLayout->addRow("Radio Button 2:", new QRadioButton("Option 2", this));

        formLayout->addRow("Check Box 1:", new QCheckBox("Agree to Terms", this));
        formLayout->addRow("Check Box 2:", new QCheckBox("Subscribe to Newsletter", this));

        formLayout->addRow("Spin Box:", new QSpinBox(this));
        formLayout->addRow("Double Spin Box:", new QDoubleSpinBox(this));

        formLayout->addRow("Horizontal Slider:", new QSlider(Qt::Horizontal, this));
        formLayout->addRow("Scroll Bar:", new QScrollBar(Qt::Horizontal, this));

        formLayout->addRow("Progress Bar:", new QProgressBar(this));
        formLayout->addRow("Text Edit:", new QTextEdit(this));

        formLayout->addRow("Dial:", new QDial(this));

        formLayout->addRow("Date Edit:", new QDateEdit(this));
        formLayout->addRow("Time Edit:", new QTimeEdit(this));
        formLayout->addRow("DateTime Edit:", new QDateTimeEdit(this));

        formLayout->addRow("Tab Widget:", createTabWidget());

        // Set layout for the widget
        setLayout(formLayout);
        setWindowTitle("Capstone Form with All Qt Components");
        resize(400, 600);
    }

private:
    // Function to create ComboBox
    QComboBox* createComboBox() {
        QComboBox *comboBox = new QComboBox(this);
        comboBox->addItem("Option 1");
        comboBox->addItem("Option 2");
        comboBox->addItem("Option 3");
        return comboBox;
    }

    // Function to create ListWidget
    QListWidget* createListWidget() {
        QListWidget *listWidget = new QListWidget(this);
        listWidget->addItem("Item 1");
        listWidget->addItem("Item 2");
        listWidget->addItem("Item 3");
        return listWidget;
    }

    // Function to create TabWidget
    QTabWidget* createTabWidget() {
        QTabWidget *tabWidget = new QTabWidget(this);

        QWidget *tab1 = new QWidget();
        QWidget *tab2 = new QWidget();

        QHBoxLayout *tab1Layout = new QHBoxLayout();
        tab1Layout->addWidget(new QLabel("This is Tab 1"));
        tab1->setLayout(tab1Layout);

        QHBoxLayout *tab2Layout = new QHBoxLayout();
        tab2Layout->addWidget(new QLabel("This is Tab 2"));
        tab2->setLayout(tab2Layout);

        tabWidget->addTab(tab1, "Tab 1");
        tabWidget->addTab(tab2, "Tab 2");

        return tabWidget;
    }
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    CapstoneForm form;
    form.show();

    return app.exec();
}
```
## Output
![image](https://github.com/user-attachments/assets/0712db37-5cd3-458a-8db7-98927ed2e393)
