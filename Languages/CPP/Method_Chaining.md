#include <iostream>

class MyClass {
public:
    MyClass& setA(int a) {
        this->a = a;
        return *this;
    }

    MyClass& setB(int b) {
        this->b = b;
        return *this;
    }

    MyClass& display() {
        std::cout << "a: " << a << ", b: " << b << std::endl;
        return *this;
    }

private:
    int a, b;
};

int main() {
    MyClass obj;
    obj.setA(10).setB(20).display();
    return 0;
}
