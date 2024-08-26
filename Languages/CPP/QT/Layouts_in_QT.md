# Layouts in QT

Qt provides several layout managers to arrange widgets within a parent widget. Here’s an overview of the most important layouts:

### 1. **QVBoxLayout** (Vertical Box Layout)
- **Description**: Arranges widgets vertically in a single column.
- **Use Case**: Ideal for stacking widgets one below the other, like buttons or labels in a vertical list.

```cpp
QVBoxLayout *layout = new QVBoxLayout;
layout->addWidget(widget1);
layout->addWidget(widget2);
```

### 2. **QHBoxLayout** (Horizontal Box Layout)
- **Description**: Arranges widgets horizontally in a single row.
- **Use Case**: Best for placing widgets side by side, such as buttons or text fields in a horizontal line.

```cpp
QHBoxLayout *layout = new QHBoxLayout;
layout->addWidget(widget1);
layout->addWidget(widget2);
```

### 3. **QGridLayout** (Grid Layout)
- **Description**: Arranges widgets in a grid with rows and columns.
- **Use Case**: Useful for complex forms or tables where precise placement of widgets is needed.

```cpp
QGridLayout *layout = new QGridLayout;
layout->addWidget(widget1, 0, 0);  // Row 0, Column 0
layout->addWidget(widget2, 0, 1);  // Row 0, Column 1
```

### 4. **QFormLayout** (Form Layout)
- **Description**: Arranges widgets in a two-column form with labels in the first column and widgets in the second column.
- **Use Case**: Ideal for creating labeled forms, such as user input dialogs.

```cpp
QFormLayout *layout = new QFormLayout;
layout->addRow("Name:", nameEdit);
layout->addRow("Email:", emailEdit);
```

### 5. **QStackedLayout** (Stacked Layout)
- **Description**: Stacks widgets on top of each other; only one widget is visible at a time.
- **Use Case**: Useful for creating tab-like interfaces or wizards where different views are shown based on user interaction.

```cpp
QStackedLayout *layout = new QStackedLayout;
layout->addWidget(page1);
layout->addWidget(page2);
```

### Summary

- **QVBoxLayout** and **QHBoxLayout** are used for simple vertical or horizontal arrangements.
- **QGridLayout** offers a flexible grid for precise positioning.
- **QFormLayout** is tailored for forms with labeled fields.
- **QStackedLayout** is ideal for stacked views, like in a wizard or tabs.

Layouts help manage widget sizes and positions automatically, ensuring a consistent and adaptive user interface.
