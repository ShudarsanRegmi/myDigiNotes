Here's a more complex Qt application for a BMI (Body Mass Index) calculator with multiple UI components. The application will include input fields for weight and height, a combo box to select units, a button to calculate the BMI, and labels to display the result and a message about the BMI category.

### File Structure:
- `main.cpp`
- `MainWindow.h`
- `MainWindow.cpp`
- `BMICalculator.h`
- `BMICalculator.cpp`

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
#include <QLineEdit>
#include <QComboBox>
#include <QPushButton>
#include <QLabel>
#include <QVBoxLayout>
#include "BMICalculator.h"

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void calculateBMI();

private:
    QLineEdit *weightInput;
    QLineEdit *heightInput;
    QComboBox *unitSelector;
    QPushButton *calculateButton;
    QLabel *resultLabel;
    QLabel *categoryLabel;

    BMICalculator *calculator;
};

#endif // MAINWINDOW_H
```

### `MainWindow.cpp`
```cpp
#include "MainWindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), calculator(new BMICalculator()) {

    // Create UI components
    weightInput = new QLineEdit(this);
    heightInput = new QLineEdit(this);
    unitSelector = new QComboBox(this);
    calculateButton = new QPushButton("Calculate BMI", this);
    resultLabel = new QLabel("Your BMI: ", this);
    categoryLabel = new QLabel("", this);

    // Set placeholder text
    weightInput->setPlaceholderText("Enter weight");
    heightInput->setPlaceholderText("Enter height");

    // Populate unit selector
    unitSelector->addItem("Metric (kg, meters)");
    unitSelector->addItem("Imperial (lbs, inches)");

    // Set layout
    QVBoxLayout *layout = new QVBoxLayout();
    layout->addWidget(weightInput);
    layout->addWidget(heightInput);
    layout->addWidget(unitSelector);
    layout->addWidget(calculateButton);
    layout->addWidget(resultLabel);
    layout->addWidget(categoryLabel);

    QWidget *centralWidget = new QWidget(this);
    centralWidget->setLayout(layout);
    setCentralWidget(centralWidget);

    // Connect signal to slot
    connect(calculateButton, &QPushButton::clicked, this, &MainWindow::calculateBMI);
}

MainWindow::~MainWindow() {
    delete calculator;
}

void MainWindow::calculateBMI() {
    bool ok;
    double weight = weightInput->text().toDouble(&ok);
    if (!ok) {
        resultLabel->setText("Invalid weight input.");
        return;
    }

    double height = heightInput->text().toDouble(&ok);
    if (!ok) {
        resultLabel->setText("Invalid height input.");
        return;
    }

    bool isMetric = (unitSelector->currentIndex() == 0);
    double bmi = calculator->calculateBMI(weight, height, isMetric);
    resultLabel->setText("Your BMI: " + QString::number(bmi, 'f', 2));
    categoryLabel->setText(calculator->getBMICategory(bmi));
}
```

### `BMICalculator.h`
```cpp
#ifndef BMICALCULATOR_H
#define BMICALCULATOR_H

#include <QString>

class BMICalculator {
public:
    BMICalculator();
    double calculateBMI(double weight, double height, bool isMetric);
    QString getBMICategory(double bmi);
};

#endif // BMICALCULATOR_H
```

### `BMICalculator.cpp`
```cpp
#include "BMICalculator.h"

BMICalculator::BMICalculator() {
    // Constructor can initialize anything if necessary
}

double BMICalculator::calculateBMI(double weight, double height, bool isMetric) {
    if (!isMetric) {
        // Convert from imperial to metric
        weight *= 0.453592;  // lbs to kg
        height *= 0.0254;    // inches to meters
    }
    return weight / (height * height);
}

QString BMICalculator::getBMICategory(double bmi) {
    if (bmi < 18.5) {
        return "Underweight";
    } else if (bmi < 24.9) {
        return "Normal weight";
    } else if (bmi < 29.9) {
        return "Overweight";
    } else {
        return "Obesity";
    }
}
```

### Explanation:
- **MainWindow**: The `MainWindow` class handles the main UI and logic. It includes multiple UI components:
  - `QLineEdit` for weight and height input.
  - `QComboBox` for selecting units (Metric or Imperial).
  - `QPushButton` for triggering the BMI calculation.
  - `QLabel` for displaying the calculated BMI and the corresponding category.
  
- **BMICalculator**: The `BMICalculator` class handles the calculation of BMI and the categorization based on the BMI value.

This application demonstrates OOP principles, with UI components managed within the `MainWindow` class and the business logic encapsulated in the `BMICalculator` class. The app provides a meaningful function (BMI calculation) with a more complex UI.
