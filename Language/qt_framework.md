# Qt:  Cute not Cu-tee
> But we'll call cu-tee only | Library to build GUI(Desktop) Applications

## How is qt program compiled 
Qt Creator does the job of invoking the build system for us, but it might be interesting to know how Qt programs are compiled.

For small programs, it is easy to compile everything by hand, creating object files, then linking them. But for bigger projects, the command line easily becomes hard to write. If you are familiar with Linux, you may know that all the programs are compiled using a makefile that describes all these command lines to execute. But for some projects, even writing a makefile can become tedious.

qmake is the build system that comes with Qt, and it generates those makefiles for you (there are other build systems that can be used, but here we give an example with qmake). With a simple syntax, it produces the makefile that is used to compile a Qt program. But that is not its only purpose. Qt uses meta-objects to extend C++ functionalities, and qmake is responsible for preparing a makefile that contains this meta-object extraction phase. You will see this in another chapter.

So, Qt apps are compiled in 3 steps

A .pro file is written to describe the project to compile
A makefile is generated using qmake
The program is built using make (or nmake or jom on windows)

Qt objects have a lot of attributes that can be modified using getters and setters. In Qt, if an attribute is called foo, the associated getter and setter will have these signatures

```cpp
T foo() const;
void setFoo(const T);
```

