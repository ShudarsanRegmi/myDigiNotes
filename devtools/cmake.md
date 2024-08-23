# CMake Tutorial

CMake is a cross-platform build system that helps in managing the build process of software projects in a compiler-independent manner. It is widely used in projects written in C and C++, but it can also handle other languages. Here’s a breakdown of the key concepts to help you get started with CMake:

### **Key Concepts of CMake**

#### 1. **CMakeLists.txt**
   CMake uses a file called `CMakeLists.txt` to define the project configuration. This file specifies how the project should be built, including source files, compiler options, libraries, and more.

   Here's a basic example of a `CMakeLists.txt`:
   ```cmake
   cmake_minimum_required(VERSION 3.10)
   
   # Project Name
   project(HelloWorld)

   # Specify C++ standard
   set(CMAKE_CXX_STANDARD 11)

   # Add an executable
   add_executable(hello main.cpp)
   ```
   This example tells CMake to:
   - Require at least version 3.10 of CMake.
   - Define a project called `HelloWorld`.
   - Use the C++11 standard.
   - Compile `main.cpp` into an executable named `hello`.

#### 2. **Building with CMake**
   To build a project with CMake, follow these steps:
   
   - **Step 1: Create a Build Directory**
     Create a separate directory (e.g., `build/`) to contain the build files and the compiled binaries.
     ```bash
     mkdir build
     cd build
     ```
   
   - **Step 2: Generate Build Files**
     Inside the build directory, run CMake to generate the build files for your compiler (e.g., Makefiles for `make` or Visual Studio project files).
     ```bash
     cmake ..
     ```
     The `..` refers to the parent directory where the `CMakeLists.txt` is located.

   - **Step 3: Build the Project**
     Once the build files are generated, use a build system like `make` to build the project:
     ```bash
     make
     ```

#### 3. **Variables and Options**
   You can define variables and options in CMake to customize the build process. For example:
   ```cmake
   set(MY_VAR "Hello")
   option(USE_FEATURE "Enable a special feature" ON)
   ```
   - `set()` allows you to define a variable.
   - `option()` creates a configurable option that can be toggled ON or OFF.

#### 4. **Targets**
   In CMake, a target can be an executable, a library, or a custom command. You define targets using commands like `add_executable()` and `add_library()`.

   Example of adding a library and linking it to an executable:
   ```cmake
   add_library(my_lib SHARED my_lib.cpp)
   target_link_libraries(hello my_lib)
   ```
   This defines a shared library `my_lib` and links it to the `hello` executable.

#### 5. **Finding Packages**
   CMake allows you to find and link to external libraries using `find_package()`:
   ```cmake
   find_package(OpenSSL REQUIRED)
   target_link_libraries(hello OpenSSL::SSL)
   ```
   This finds the OpenSSL package and links the SSL component to the `hello` target.

#### 6. **Installation**
   You can define how your project should be installed on the system using the `install()` command:
   ```cmake
   install(TARGETS hello DESTINATION bin)
   install(FILES my_header.h DESTINATION include)
   ```

   This will install the `hello` executable to `bin/` and the header file to `include/`.

#### 7. **Handling Different Platforms**
   CMake makes it easy to handle different platforms by checking conditions:
   ```cmake
   if (WIN32)
     # Windows specific settings
   elseif(UNIX)
     # Unix/Linux specific settings
   endif()
   ```

### **Advantages of CMake**
- **Cross-platform**: Works on different operating systems like Linux, Windows, macOS, etc.
- **Compiler agnostic**: Works with various compilers like GCC, Clang, MSVC.
- **Modern features**: Supports modern C++ standards and easily integrates with external libraries.
- **Flexibility**: Allows for custom build targets and build options.

### **Example Project Structure**
```
MyProject/
│
├── CMakeLists.txt
├── src/
│   ├── main.cpp
│   └── my_lib.cpp
├── include/
│   └── my_header.h
└── build/      # Build artifacts (not in version control)
```

### **CMake Tools and Extensions**
- **CCMake**: A curses-based terminal GUI for configuring CMake options.
- **CMake GUI**: A graphical interface for setting up and configuring the build system.
- **CPack**: An extension of CMake that allows you to create installers and packages for your project.

With this introduction, you can start building your C++ projects using CMake!
