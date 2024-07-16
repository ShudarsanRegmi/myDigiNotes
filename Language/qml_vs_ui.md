# .qml vs. .ui files
In Qt development, `.qml` and `.ui` are two different file types used for designing user interfaces, but they serve different purposes and are used in different contexts.

### .qml Files

- **Purpose**: `.qml` files are used in Qt Quick, which is a module for developing modern, fluid, animated user interfaces with a declarative language called QML (Qt Modeling Language).
- **Usage**: 
  - QML is a declarative language that makes it easy to build dynamic and interactive UIs.
  - It is particularly suitable for applications that require a rich user experience with animations and transitions.
  - QML files can be combined with JavaScript for logic and data processing.

### .ui Files

- **Purpose**: `.ui` files are used in the traditional Qt Widgets module, which is based on C++ and provides a more conventional approach to building user interfaces with widgets.
- **Usage**:
  - `.ui` files are XML files that describe the layout and properties of widgets in a form.
  - They are created and edited using Qt Designer, a visual tool integrated into Qt Creator.
  - The `.ui` files are converted into C++ code by the `uic` (User Interface Compiler) when the project is built.
  - These files are part of projects that use the Qt Widgets module, where the user interface is composed of widgets like buttons, labels, text fields, etc.

### Differences and Use Cases

1. **Design Philosophy**:
   - **QML**: Declarative and suitable for highly dynamic and animated UIs.
   - **UI**: Descriptive and suited for traditional desktop applications with static or moderately dynamic UIs.

2. **Integration with Code**:
   - **QML**: Integrated with JavaScript and C++. You can write logic in JavaScript within the QML files or connect to C++ backend using Qt's integration features.
   - **UI**: Integrated with C++. The `.ui` files are used with C++ classes that define the behavior and logic of the widgets.

3. **Development Tools**:
   - **QML**: Edited using text editors or Qt Creator's QML editor.
   - **UI**: Edited using Qt Designer, a WYSIWYG editor.

### Example Project Using .ui Files

In the provided image, the project structure is as follows:

1. **proj1.pro**: The project file that contains the build configuration.
2. **Headers**:
   - `mainwindow.h`: The header file for the main window class.
3. **Sources**:
   - `main.cpp`: The main entry point of the application.
   - `mainwindow.cpp`: The source file for the main window class.
4. **Forms**:
   - `mainwindow.ui`: The UI file that defines the layout and widgets of the main window.

### Creating a TODO List App Using .ui Files

If you are using `.ui` files, here is a step-by-step guide to create a TODO list app:

1. **Design the Main Window in Qt Designer**:
   - Open `mainwindow.ui` in Qt Designer.
   - Add a `QListWidget` to display the TODO items.
   - Add a `QLineEdit` for inputting new TODO items.
   - Add a `QPushButton` for adding items to the list.

2. **Set Up the Main Window Class**:
   - In `mainwindow.h`, declare slots for adding and removing items.
   - In `mainwindow.cpp`, implement the logic for these slots.

3. **Connect Signals and Slots**:
   - Connect the `clicked` signal of the add button to the slot that adds a new item.
   - Connect the `itemClicked` signal of the list widget to a slot that toggles the completion status or removes items.

4. **Implement Data Persistence (Optional)**:
   - Use `QSettings`, a file-based storage, or a database to save and load TODO items between sessions.

By understanding the differences between `.qml` and `.ui` files and their respective uses, you can choose the right tool for your project's requirements.
