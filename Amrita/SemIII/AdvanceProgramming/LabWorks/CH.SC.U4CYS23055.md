# Lab - 1

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>


## Task - 1
```cpp
/* You are given two strings, a, and b, separated by a new line. Each string will consist of lower case alphabets.
In the first line print two space-separated integers, representing the length of a and b respectively.
In the second line print the string produced by concatenating a and b.
In the third line print two strings separated by a space, a' and b'.  a' and b' are the same as a and b, respectively, except that their first characters are swapped.
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
	string str1;
	string str2;
	
	cin>>str1;
	cin>>str2;
	cout<< str1.length() << " " << str2.length()<<endl;
	cout<< str1+str2<<endl;

	string str3;
	string str4;
	str3 = str1;
	str4 = str2;
	str3[0] = str2[0];
	str4[0] = str1[0];
	cout << str3 << " " << str4 << endl;

	return 0;
}
```
### Output
```output
▶ ./out
hari
lal
4 3
harilal
lari hal
```

## Task - 2
```cpp
/*
2. We can store details related to a student in a class consisting of his age (int), first_name (string), last_name (string) and standard (int).
You must create a class, named Student, representing the student's details, as mentioned above, and store the data of a student. Create setter and getter functions for each element; that is, the class should at least have following functions:
get_age, set_age
get_first_name, set_first_name
get_last_name, set_last_name
get_standard, set_standard
*/

#include <iostream>
#include <string>

using namespace std;

class Student {
	private:
		string fname;
		string lname;
		int age;
		int cls;
	public:
		int roll;
		int stuCount;

	Student(string fname, string lname, int age, int cls, int roll) {
		this->fname = fname;
		this->lname = lname;
		this->age = age;
		this->cls = cls;
		this->roll = roll;
		stuCount++;
	}

	string get_fname() {
		return this->fname;
	}

	void set_fname(string fname) {
		this->fname = fname;
	}

	string get_lname() {
		return this->lname;
	}

	void set_lname(string lname) {
		this->lname = lname;
	}

	int get_age() {
		return this->age;
	}

	void set_age(int age) {
		this->age= age;
	}
	
	int get_cls() {
		return this->cls;
	}

	void set_cls(int cls) {
		this->cls = cls;
	}
};

int main() {
	Student stu0("ram", "lal", 20, 12,55);
	
	// Accessing public data members
	cout << "Roll: " << stu0.roll << endl;
	cout << "stuCount: " << stu0.stuCount << endl;
	
	// Accessing public data members with getters
	cout << "First Name: " << stu0.get_fname() << endl;
	cout << "Last Name: " << stu0.get_lname() << endl;
	cout << "Age: " << stu0.get_age() << endl;
	cout << "Class: " << stu0.get_cls() << endl;
	
	// Using setters to modify private data members
	cout << "--------" << endl;
	stu0.set_fname("ravan");
	cout << "First Name: " << stu0.get_fname() << endl;

	return 0;
}
```
### Output
```
▶ ./out
Roll: 55
stuCount: 31274#include <iostream>
#include <string>

using namespace std;

class Worker {
private:
    int id;
    string name;
    char group;
    double hoursWorked;
    double wage;
    static const double nominalPayRate; // Sensitive data

public:
    // Default constructor
    Worker() : id(0), name(""), group(' '), hoursWorked(0.0), wage(0.0) {}

    // Parameterized constructor
    Worker(int workerId, const string& workerName, char workerGroup) {
        this->id = workerId;
        this->name = workerName;
        this->group = workerGroup;
        this->hoursWorked = 0.0; // Initialize hours worked to 0
        this->wage = 0.0; // Initialize wage to 0
    }

    // Accessors (Getters)
    int getId() const {
        return id;
    }

    string getName() const {
        return name;
    }

    char getGroup() const {
        return group;
    }

    double getHoursWorked() const {
        return hoursWorked;
    }

    double getWage() const {
        return wage;
    }

    // Mutators (Setters)
    void setId(int workerId) {
        id = workerId;
    }

    void setName(const string& workerName) {
        name = workerName;
    }

    void setGroup(char workerGroup) {
        group = workerGroup;
    }

    void setHoursWorked(double hours) {
        if (hours >= 0) {
            hoursWorked = hours;
        } else {
            cerr << "Hours worked cannot be negative.\n";
        }
    }

    void computeWage() {
        wage = hoursWorked * Worker::nominalPayRate; // Accessing static constant using scope resolution operator
    }

    // Display worker details
    void displayWorkerDetails() const {
        cout << "Worker ID: " << id << "\n";
        cout << "Worker Name: " << name << "\n";
        cout << "Worker Group: " << group << "\n";
        cout << "Hours Worked: " << hoursWorked << "\n";
        cout << "Weekly Wage: $" << wage << "\n";
    }
};

// Definition of the static nominalPayRate
const double Worker::nominalPayRate = 20.0; // $20 per hour

int main() {
    int n;
    cout << "Enter number of workers: ";
    cin >> n;

    // Initializing an array of Worker objects
    Worker workers[3] = {
        Worker(1, "Ram", 'A'),
        Worker(2, "Shyam", 'B'),
        Worker(3, "Hari", 'C'),
    };

    workers[0].setHoursWorked(5);
    workers[1].setHoursWorked(7);
    workers[2].setHoursWorked(2);

    // Compute wages and display worker details
    for (int i = 0; i < 3; ++i) {
        workers[i].computeWage();
        workers[i].displayWorkerDetails();
        cout << endl;
    }

    return 0;
}

First Name: ram
Last Name: lal
Age: 20
Class: 12
--------
First Name: ravan
```
## Task - 3
```cpp
/* 3. Create the student class with the following data members: student_name, roll_num, marks1, marks2. Take name, roll number, marks1 and marks2 information from user. Calculate the mean value of marks and display student_name, roll_num, mean mark values. */

#include <iostream>
#include <string>


using namespace std;

class Student {
	public:
		string student_name;
		int roll;
		int mark1;
		int mark2;
		float mean;

	Student(string name, int roll, int mark1, int mark2) {
		this->student_name=name;
		this->roll=roll;
		this->mark1=mark1;
		this->mark2=mark2;
	}
	void display_result() {
		this->mean = (mark1+mark2)/2;
		
		cout << "Name: " << this->student_name << endl;
		cout << "Roll : " << this->roll << endl;
		cout << "Mean marks: " << this->mean << endl;

	}


};

int main() {
	Student stu0("Ram", 55, 20, 30);
	stu0.display_result();
	return 0;
}

```
### Output
```
▶ ./out
Name: Ram
Roll : 55
Mean marks: 25
```

### Task - 4
```cpp
/*
4. Create the Worker class mentioning their id, name, and group (A or B or C) to which they belong. Compute their weekly wages for the number of hours they work, fixing a nominal pay rate which is a sensitive data. Include the Accessor and mutator member functions to set and display the wages.
*/

#include <iostream>
#include <string>

using namespace std;

class Worker {
private:
    int id;
    string name;
    char group;
    double hoursWorked;
    double wage;
    static const double nominalPayRate; // Sensitive data

public:
    // Constructor
    Worker(int workerId, string  workerName, char workerGroup) {
			this->id = workerId;
			this->name = workerName;
			this->group = workerGroup;
	}


    // Accessors (Getters)
    int getId() const {
        return id;
    }

    string getName() const {
        return name;
    }

    char getGroup() const {
        return group;
    }

    double getHoursWorked() const {
        return hoursWorked;
    }

    double getWage() const {
        return wage;
    }

    // Mutators (Setters)
    void setId(int workerId) {
        id = workerId;
    }

    void setName(const string& workerName) {
        name = workerName;
    }

    void setGroup(char workerGroup) {
        group = workerGroup;
    }

    void setHoursWorked(double hours) {
        if(hours >= 0) {
            hoursWorked = hours;
        } else {
            cerr << "Hours worked cannot be negative.\n";
        }
    }

    void computeWage() {
        wage = hoursWorked * nominalPayRate;
    }

    // Display worker details
    void displayWorkerDetails() const {
        cout << "Worker ID: " << id << "\n";
        cout << "Worker Name: " << name << "\n";
        cout << "Worker Group: " << group << "\n";
        cout << "Hours Worked: " << hoursWorked << "\n";
        cout << "Weekly Wage: $" << wage << "\n";
    }
};

// Definition of the static nominalPayRate
const double Worker::nominalPayRate = 20.0; // $20 per hour

int main() {
    Worker worker1(1, "Falano Diskano", 'A');
    worker1.setHoursWorked(40); // Set hours worked
    worker1.computeWage(); // Compute the wage
    worker1.displayWorkerDetails(); // Display worker details
    return 0;
}

```
### Output
```
▶ ./out
Worker ID: 1
Worker Name: Falano Diskano
Worker Group: A
Hours Worked: 40
Weekly Wage: $800
```
## Task - 5

**Approach-1***
```cpp
#include <iostream>
#include <string>

using namespace std;

class Worker {
private:
    int id;
    string name;
    char group;
    double hoursWorked;
    double wage;
    static const double nominalPayRate; // Sensitive data

public:
    // Default constructor
    Worker() : id(0), name(""), group(' '), hoursWorked(0.0), wage(0.0) {}

    // Parameterized constructor
    Worker(int workerId, const string& workerName, char workerGroup) {
        this->id = workerId;
        this->name = workerName;
        this->group = workerGroup;
        this->hoursWorked = 0.0; // Initialize hours worked to 0
        this->wage = 0.0; // Initialize wage to 0
    }

    // Accessors (Getters)
    int getId() const {
        return id;
    }

    string getName() const {
        return name;
    }

    char getGroup() const {
        return group;
    }

    double getHoursWorked() const {
        return hoursWorked;
    }

    double getWage() const {
        return wage;
    }

    // Mutators (Setters)
    void setId(int workerId) {
        id = workerId;
    }

    void setName(const string& workerName) {
        name = workerName;
    }

    void setGroup(char workerGroup) {
        group = workerGroup;
    }

    void setHoursWorked(double hours) {
        if (hours >= 0) {
            hoursWorked = hours;
        } else {
            cerr << "Hours worked cannot be negative.\n";
        }
    }

    void computeWage() {
        wage = hoursWorked * Worker::nominalPayRate; // Accessing static constant using scope resolution operator
    }

    // Display worker details
    void displayWorkerDetails() const {
        cout << "Worker ID: " << id << "\n";
        cout << "Worker Name: " << name << "\n";
        cout << "Worker Group: " << group << "\n";
        cout << "Hours Worked: " << hoursWorked << "\n";
        cout << "Weekly Wage: $" << wage << "\n";
    }
};

// Definition of the static nominalPayRate
const double Worker::nominalPayRate = 20.0; // $20 per hour

int main() {
    int n;
    cout << "Enter number of workers: ";
    cin >> n;

    // Initializing an array of Worker objects
    Worker workers[3] = {
        Worker(1, "Ram", 'A'),
        Worker(2, "Shyam", 'B'),
        Worker(3, "Hari", 'C'),
    };

    workers[0].setHoursWorked(5);
    workers[1].setHoursWorked(7);
    workers[2].setHoursWorked(2);

    // Compute wages and display worker details
    for (int i = 0; i < 3; ++i) {
        workers[i].computeWage();
        workers[i].displayWorkerDetails();
        cout << endl;
    }

    return 0;
}

```

**Approach-2**
```cpp
/*
Do Task with Array.
*/
#include <iostream>
#include <string>

using namespace std;

class Worker {
private:
    int id;
    string name;
    char group;
    double hoursWorked;
    double wage;
    static const double nominalPayRate; // Sensitive data

public:
    // Default constructor
    Worker() : id(0), name(""), group(' '), hoursWorked(0.0), wage(0.0) {}

    // Parameterized constructor
    Worker(int workerId, const string& workerName, char workerGroup) {
        this->id = workerId;
        this->name = workerName;
        this->group = workerGroup;
        this->hoursWorked = 0.0; // Initialize hours worked to 0
        this->wage = 0.0; // Initialize wage to 0
    }

    // Accessors (Getters)
    int getId() const {
        return id;
    }

    string getName() const {
        return name;
    }

    char getGroup() const {
        return group;
    }

    double getHoursWorked() const {
        return hoursWorked;
    }

    double getWage() const {
        return wage;
    }

    // Mutators (Setters)
    void setId(int workerId) {
        id = workerId;
    }

    void setName(const string& workerName) {
        name = workerName;
    }

    void setGroup(char workerGroup) {
        group = workerGroup;
    }

    void setHoursWorked(double hours) {
        if (hours >= 0) {
            hoursWorked = hours;
        } else {
            cerr << "Hours worked cannot be negative.\n";
        }
    }

    void computeWage() {
        wage = hoursWorked * Worker::nominalPayRate; // Accessing static constant using scope resolution operator
    }

    // Display worker details
    void displayWorkerDetails() const {
        cout << "Worker ID: " << id << "\n";
        cout << "Worker Name: " << name << "\n";
        cout << "Worker Group: " << group << "\n";
        cout << "Hours Worked: " << hoursWorked << "\n";
        cout << "Weekly Wage: $" << wage << "\n";
    }
};

// Definition of the static nominalPayRate
const double Worker::nominalPayRate = 20.0; // $20 per hour

int main() {
    int n;
    cout << "Enter number of workers: ";
    cin >> n;

    // Create an array of pointers to Worker objects
    Worker* workers[n];

    for (int i = 0; i < n; ++i) {
        int id;
        string name;
        char group;
        double hrsWorked;

        cout << "Enter worker ID: ";
        cin >> id;

        cout << "Enter worker name: ";
        cin.ignore(); // To ignore any newline character left in the input buffer
        getline(cin, name);

        cout << "Enter worker group (A, B, or C): ";
        cin >> group;

        cout << "Enter hours worked: ";
        cin >> hrsWorked;

        // Allocate memory for each Worker object
        workers[i] = new Worker(id, name, group);
        workers[i]->setHoursWorked(hrsWorked);
        workers[i]->computeWage();
        workers[i]->displayWorkerDetails();
    }

    // Free dynamically allocated memory
    for (int i = 0; i < n; ++i) {
        delete workers[i];
    }

    return 0;
}
```

### Output

```
▶ ./out
Enter number of workers: 2
Enter worker ID: 1234
Enter worker name: ram
Enter worker group (A, B, or C): A
Enter hours worked: 3 
Worker ID: 1234
Worker Name: ram
Worker Group: A
Hours Worked: 3
Weekly Wage: $60
Enter worker ID: 44
Enter worker name: shyam
Enter worker group (A, B, or C): C
Enter hours worked: 23
Worker ID: 44
Worker Name: shyam
Worker Group: C
Hours Worked: 23
Weekly Wage: $460

```

## Task-6

```cpp
#include <iostream>

using namespace std;

class Student {

	public:
		int scores[5];
		

		Student() {
			// creating new student

		}

		void input() {
			for(int i=0; i<5; i++) {
				cout << "Enter the marks: " << endl;
				cin >>  scores[i];
			}
		}

		int calculateScore() {
			int sum = 0;
			for (int i=0; i<5; i++) {
				sum+= scores[i];
			}

			return sum;
		}
};


int main() {

	Student st0 = Student();
	st0.input();
	cout << "-------------------" << endl;

	Student st1 = Student();
	st1.input();
	cout << "-------------------" << endl;

	Student st2 = Student();
	st2.input();
	cout << "-------------------" << endl;

	Student st3 = Student();
	st3.input();
	cout << "-------------------" << endl;

	Student st4 = Student();
	st4.input();
	cout << "-------------------" << endl;

	Student studs[5] = {st0, st1, st2, st3, st4};
	
	cout << st0.calculateScore();


	// suppose i'm stu
	cout << "Enter your marks: " << endl;	
	Student stu = Student();
	stu.input();
	int mytot = stu.calculateScore();	

	int c=0;	
	for (int i=0; i<5; i++) {
		if (studs[i].calculateScore() > mytot) {
			c+=1;
		}
	}

	cout << "No of student whose marks is more than me in my class: " << c << endl;

	return 0;
}

```

## Answer
```cpp
No of student whose marks is more than me in my class: 2
```

# Lab  -2

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>



## Task -1 
```cpp
/*
1. Create a class 'Student' with three data members which are name, age and address. The constructor of the class assigns
 default values to name as "unknown", age as '0' and address as "not available". It has two functions with the same name
'setInfo'. First function has two parameters for name and age and assigns the same whereas the second function takes has
three parameters which are assigned to name, age and address respectively. Print the name, age and address of 10 students
*/
#include <iostream>
#include <string>

using namespace std;

class Student {
private:
    string name;
    int age;
    string address;

public:
    // Constructor with default values
    Student() : name("unknown"), age(0), address("not available") {}

    // Function to set name and age
    void setInfo(string n, int a) {
        name = n;
        age = a;
    }

    // Function to set name, age, and address
    void setInfo(string n, int a, string addr) {
        name = n;
        age = a;
        address = addr;
    }

    // Function to print student details
    void printInfo() const {
        cout << "Name: " << name << ", Age: " << age << ", Address: " << address << endl;
    }
};

int main() {
    // Array of 10 students
    Student students[10];

    // Setting info for students with Indian names
    students[0].setInfo("Amit", 20);
    students[1].setInfo("Priya", 22, "123 MG Road, Mumbai");
    students[2].setInfo("Rahul", 21, "456 Brigade Road, Bangalore");
    students[3].setInfo("Sita", 23);
    students[4].setInfo("Ravi", 24, "789 Anna Salai, Chennai");
    students[5].setInfo("Anjali", 19);
    students[6].setInfo("Vikram", 25, "101 Park Street, Kolkata");
    students[7].setInfo("Meera", 22);
    students[8].setInfo("Arjun", 26, "321 Connaught Place, Delhi");
    students[9].setInfo("Radha", 18);

    // Print info for all students
    for (int i = 0; i < 10; ++i) {
        students[i].printInfo();
    }

    return 0;
}

```
### Output
```bash
g++ -o out task1.cpp
./out
Name: Amit, Age: 20, Address: not available
Name: Priya, Age: 22, Address: 123 MG Road, Mumbai
Name: Rahul, Age: 21, Address: 456 Brigade Road, Bangalore
Name: Sita, Age: 23, Address: not available
Name: Ravi, Age: 24, Address: 789 Anna Salai, Chennai
Name: Anjali, Age: 19, Address: not available
Name: Vikram, Age: 25, Address: 101 Park Street, Kolkata
Name: Meera, Age: 22, Address: not available
Name: Arjun, Age: 26, Address: 321 Connaught Place, Delhi
Name: Radha, Age: 18, Address: not available
```

## Task -2 

```cpp
/*
2. Create a class named 'complex' with two data members- real and imag and a function to display the value which is in the
form of 'a+ib'.
*/
#include <iostream>

using namespace std;

class Complex {
private:
    float real;
    float imag;

public:
    // Constructor to initialize the real and imaginary parts
    Complex(float r = 0.0, float i = 0.0) : real(r), imag(i) {}

    // Function to display the complex number in the form 'a + ib'
    void display() const {
        cout << real << " + " << imag << "i" << endl;
    }
};

int main() {
    // Create complex number objects
    Complex c1(3.5, 2.5);
    Complex c2(1.2, 3.8);

    // Display the complex numbers
    c1.display();  // Output: 3.5 + 2.5i
    c2.display();  // Output: 1.2 + 3.8i

    return 0;
}

```

```bash
g++ -o out task2.cpp
./out
3.5 + 2.5i
1.2 + 3.8i
```

## Task - 3

```cpp
/*
3. Create a Time class with hours and minutes data members. Create two time objects. Write a member function to add these
two time objects. See that this member function takes two time objects as parameters. Demonstrate your code with appropriate
messages.
*/
#include <iostream>

using namespace std;

class Time {
private:
    int hours;
    int minutes;

public:
    // Constructor to initialize hours and minutes
    Time(int h = 0, int m = 0) : hours(h), minutes(m) {}

    // Function to add two Time objects
    void addTime(Time t1, Time t2) {
        // Add the minutes and hours of both time objects
        minutes = t1.minutes + t2.minutes;
        hours = t1.hours + t2.hours;

        // If minutes exceed 60, convert it into hours
        if (minutes >= 60) {
            hours += minutes / 60;
            minutes = minutes % 60;
        }
    }

    // Function to display the time in hours and minutes
    void display() const {
        cout << "Time: " << hours << " hours and " << minutes << " minutes." << endl;
    }
};

int main() {
    // Creating two time objects
    Time t1(2, 50);  // 2 hours and 50 minutes
    Time t2(1, 30);  // 1 hour and 30 minutes

    // Display initial times
    cout << "First Time Object: ";
    t1.display();

    cout << "Second Time Object: ";
    t2.display();

    // Creating a third time object to store the result of addition
    Time t3;

    // Adding two time objects
    t3.addTime(t1, t2);

    // Display the result
    cout << "After Adding Time Objects: ";
    t3.display();

    return 0;
}

```

### Output

```bash
g++ -o out task3.cpp
./out
First Time Object: Time: 2 hours and 50 minutes.
Second Time Object: Time: 1 hours and 30 minutes.
After Adding Time Objects: Time: 4 hours and 20 minutes.
```

## Task - 4
```cpp
/*
4. Write a C++ program that uses an area() function for the calculation of area of a triangle or a rectangle or a square.
 Number of sides (3 for a triangle, 2 for a rectangle and 1 for a square) suggest about the shape for which area is to be
calculated.
*/
#include <iostream>
#include <cmath>  // For sqrt() function to calculate triangle area

using namespace std;

// Function to calculate the area of triangle, rectangle, or square
void area(int sides) {
    if (sides == 3) {
        // Triangle
        double base, height;
        cout << "Enter the base and height of the triangle: ";
        cin >> base >> height;
        double triangleArea = (base * height) / 2;
        cout << "Area of the triangle: " << triangleArea << endl;

    } else if (sides == 2) {
        // Rectangle
        double length, width;
        cout << "Enter the length and width of the rectangle: ";
        cin >> length >> width;
        double rectangleArea = length * width;
        cout << "Area of the rectangle: " << rectangleArea << endl;

    } else if (sides == 1) {
        // Square
        double side;
        cout << "Enter the side of the square: ";
        cin >> side;
        double squareArea = side * side;
        cout << "Area of the square: " << squareArea << endl;

    } else {
        cout << "Invalid input! Number of sides must be 1, 2, or 3." << endl;
    }
}

int main() {
    int sides;

    cout << "Enter the number of sides (3 for triangle, 2 for rectangle, 1 for square): ";
    cin >> sides;

    // Call the area function
    area(sides);

    return 0;
}

```
### Output

```bash
g++ -o out task4.cpp
./out
Enter the number of sides (3 for triangle, 2 for rectangle, 1 for square): 3
Enter the base and height of the triangle: 5
2
Area of the triangle: 5
```


## Lab - 3

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>


## Task - 1

```cpp
/*
Create a class Box having length, breadth and height as private data members and count as static data member. The class uses a
constant member function getvolume() to return the product of length, breadth and height. The class uses static member function to
return the count of boxes created.
*/
#include <iostream>

using namespace std;

class Box {
private:
    double length, breadth, height; // Private data members
    static int count; // Static data member to keep track of the number of boxes created

public:
    // Constructor to initialize length, breadth, and height
    Box(double l, double b, double h) : length(l), breadth(b), height(h) {
        count++;  // Increment count each time a box is created
    }

    // Constant member function to calculate and return the volume of the box
    double getVolume() const {
        return length * breadth * height;
    }

    // Static member function to return the count of boxes created
    static int getCount() {
        return count;
    }
};

// Initialize the static data member
int Box::count = 0;

int main() {
    // Creating objects of the Box class
    Box box1(2.5, 3.0, 4.0);
    Box box2(1.5, 2.0, 3.0);
    Box box3(3.0, 3.5, 2.0);

    // Display the volumes of the boxes
    cout << "Volume of Box 1: " << box1.getVolume() << endl;
    cout << "Volume of Box 2: " << box2.getVolume() << endl;
    cout << "Volume of Box 3: " << box3.getVolume() << endl;

    // Display the count of boxes created
    cout << "Total number of boxes created: " << Box::getCount() << endl;

    return 0;
}
```
### Output

```bash
g++ -o out task5.cpp
./out
Volume of Box 1: 30
Volume of Box 2: 9
Volume of Box 3: 21
Total number of boxes created: 3
```

## Lab - 4

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>


```cpp
/*
1. You are required to design a class named FileHandler that handles basic file operations like
opening, writing to, and closing a file. This class should demonstrate the concepts of resource
management in C++ by utilizing constructors and destructors.
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class FileHandler {
private:
    ofstream file; // File stream object

public:
    // Constructor to open a file
    FileHandler(const string& fileName) {
        file.open(fileName, ios::out | ios::app); // Open the file in append mode
        if (file.is_open()) {
            cout << "File opened successfully: " << fileName << endl;
        } else {
            cerr << "Failed to open the file: " << fileName << endl;
        }
    }

    // Function to write data to the file
    void writeToFile(const string& data) {
        if (file.is_open()) {
            file << data << endl;
            cout << "Data written to file." << endl;
        } else {
            cerr << "File is not open. Cannot write data." << endl;
        }
    }

    // Destructor to close the file
    ~FileHandler() {
        if (file.is_open()) {
            file.close(); // Close the file when the object goes out of scope
            cout << "File closed successfully." << endl;
        }
    }
};

int main() {
    // Create a FileHandler object, open the file, and write to it
    FileHandler fh("example.txt");

    // Write some data to the file
    fh.writeToFile("This is the first line.");
    fh.writeToFile("This is the second line.");

    // Destructor will automatically close the file when fh goes out of scope
    return 0;
}

```

```bash
g++ -o out task1.cpp
./out
File opened successfully: example.txt
Data written to file.
Data written to file.
File closed successfully.
cat example.txt
This is the first line.
This is the second line.
```

## Task - 2
```cpp
/*
2. You are required to design a class named DynamicClass that demonstrates dynamic memory
allocation for an array of integers. The class should manage memory allocation and deallocation
efficiently using constructors and destructors
*/

#include <iostream>

using namespace std;

class DynamicClass {
private:
    int* array;      // Pointer to dynamically allocated array
    int size;        // Size of the array

public:
    // Constructor to allocate memory for the array
    DynamicClass(int s) : size(s) {
        array = new int[size]; // Allocate memory for the array
        if (array) {
            cout << "Memory allocated for array of size " << size << endl;
        } else {
            cerr << "Memory allocation failed!" << endl;
        }
    }

    // Function to set values in the array
    void setValues() {
        if (array) {
            cout << "Enter " << size << " integer values:" << endl;
            for (int i = 0; i < size; ++i) {
                cin >> array[i];
            }
        }
    }

    // Function to display values of the array
    void displayValues() const {
        if (array) {
            cout << "Array values are:" << endl;
            for (int i = 0; i < size; ++i) {
                cout << array[i] << " ";
            }
            cout << endl;
        }
    }

    // Destructor to deallocate memory
    ~DynamicClass() {
        delete[] array; // Deallocate memory
        cout << "Memory deallocated." << endl;
    }
};

int main() {
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;

    // Create a DynamicClass object
    DynamicClass obj(size);

    // Set and display values
    obj.setValues();
    obj.displayValues();

    // Destructor will automatically deallocate memory when obj goes out of scope
    return 0;
}

```

### Output

```bash
g++ -o out task2.cpp
./out
Enter the size of the array: 5
Memory allocated for array of size 5
Enter 5 integer values:
1
2
3
4
5
Array values are:
1 2 3 4 5
Memory deallocated.

```

## Task - 3

```cpp
/*
3. You are required to design a class named MyClass that demonstrates the concepts of
constructors, copy constructors, and passing objects by value
*/
#include <iostream>

using namespace std;

class MyClass {
private:
    int* data; // Pointer to dynamically allocated memory
    int size;  // Size of the data

public:
    // Default Constructor
    MyClass() : data(nullptr), size(0) {
        cout << "Default Constructor Called" << endl;
    }

    // Parameterized Constructor
    MyClass(int s) : size(s) {
        data = new int[size]; // Allocate memory
        for (int i = 0; i < size; ++i) {
            data[i] = i; // Initialize data
        }
        cout << "Parameterized Constructor Called" << endl;
    }

    // Copy Constructor
    MyClass(const MyClass& other) : size(other.size) {
        data = new int[size]; // Allocate new memory
        for (int i = 0; i < size; ++i) {
            data[i] = other.data[i]; // Copy data from other object
        }
        cout << "Copy Constructor Called" << endl;
    }

    // Destructor
    ~MyClass() {
        delete[] data; // Deallocate memory
        cout << "Destructor Called" << endl;
    }

    // Function to display data
    void display() const {
        for (int i = 0; i < size; ++i) {
            cout << data[i] << " ";
        }
        cout << endl;
    }

    // Function to demonstrate passing objects by value
    void processByValue(MyClass obj) const {
        cout << "Processing by value:" << endl;
        obj.display(); // Display copied data
    }
};

int main() {
    // Using default constructor
    MyClass obj1;
    
    // Using parameterized constructor
    MyClass obj2(5);
    obj2.display(); // Display data of obj2

    // Using copy constructor
    MyClass obj3 = obj2;
    obj3.display(); // Display data of obj3

    // Passing object by value
    obj2.processByValue(obj3);

    // Destructor will be called automatically for obj1, obj2, and obj3
    return 0;
}


```

### Output
```bash
g++ -o out task3.cpp
.%                                                                              
./out
Default Constructor Called
Parameterized Constructor Called
0 1 2 3 4
Copy Constructor Called
0 1 2 3 4
Copy Constructor Called
Processing by value:
0 1 2 3 4
Destructor Called
Destructor Called
Destructor Called
Destructor Called
```

# Lab - 5

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>


```cpp
/*
1. You are required to design two classes, one and two, that demonstrate the use of a friend
function to access and manipulate private members from both classes
*/

#include <iostream>

using namespace std;

// Forward declaration of the class Two
class Two;

// Class One
class One {
private:
    int dataOne;

public:
    // Constructor to initialize dataOne
    One(int value) : dataOne(value) {}

    // Friend function declaration to allow access to private members of both classes
    friend void displayData(const One& objOne, const Two& objTwo);

    // Function to set dataOne
    void setDataOne(int value) {
        dataOne = value;
    }
};

// Class Two
class Two {
private:
    int dataTwo;

public:
    // Constructor to initialize dataTwo
    Two(int value) : dataTwo(value) {}

    // Friend function declaration to allow access to private members of both classes
    friend void displayData(const One& objOne, const Two& objTwo);

    // Function to set dataTwo
    void setDataTwo(int value) {
        dataTwo = value;
    }
};

// Friend function definition
void displayData(const One& objOne, const Two& objTwo) {
    cout << "Data in One: " << objOne.dataOne << endl;
    cout << "Data in Two: " << objTwo.dataTwo << endl;
}

int main() {
    // Create objects of classes One and Two
    One objOne(10);
    Two objTwo(20);

    // Display initial data
    cout << "Initial data:" << endl;
    displayData(objOne, objTwo);

    // Modify data using member functions
    objOne.setDataOne(100);
    objTwo.setDataTwo(200);

    // Display updated data
    cout << "Updated data:" << endl;
    displayData(objOne, objTwo);

    return 0;
}

```

### Output

```bash
g++ -o out task1.cpp
./out
Initial data:
Data in One: 10
Data in Two: 20
Updated data:
Data in One: 100
Data in Two: 200
```

## Task - 2

```cpp
/*
2. You are required to design two classes, one and two, that demonstrate the use of a friend
function to compare the private members of both classes and determine the maximum value.
*/

#include <iostream>

using namespace std;

// Forward declaration of the class Two
class Two;

// Class One
class One {
private:
    int dataOne;

public:
    // Constructor to initialize dataOne
    One(int value) : dataOne(value) {}

    // Friend function declaration to compare private members of both classes
    friend int findMax(const One& objOne, const Two& objTwo);

    // Function to set dataOne
    void setDataOne(int value) {
        dataOne = value;
    }
};

// Class Two
class Two {
private:
    int dataTwo;

public:
    // Constructor to initialize dataTwo
    Two(int value) : dataTwo(value) {}

    // Friend function declaration to compare private members of both classes
    friend int findMax(const One& objOne, const Two& objTwo);

    // Function to set dataTwo
    void setDataTwo(int value) {
        dataTwo = value;
    }
};

// Friend function definition
int findMax(const One& objOne, const Two& objTwo) {
    // Compare private members of both classes and return the maximum
    return (objOne.dataOne > objTwo.dataTwo) ? objOne.dataOne : objTwo.dataTwo;
}

int main() {
    // Create objects of classes One and Two
    One objOne(10);
    Two objTwo(20);

    // Display initial maximum value
    cout << "Initial maximum value: " << findMax(objOne, objTwo) << endl;

    // Modify data using member functions
    objOne.setDataOne(30);
    objTwo.setDataTwo(25);

    // Display updated maximum value
    cout << "Updated maximum value: " << findMax(objOne, objTwo) << endl;

    return 0;
}

```

### Output
```bash
g++ -o out task2.cpp
./out
Initial maximum value: 20
Updated maximum value: 30
```

# Lab - 06

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>



---

## Advanced Programming Worksheet-06

### 1. Create two classes DM and DB which store the value of distances:
- DM stores distances in meters and centimeters, and DB in feet and inches.
- Write a program that reads values for the class objects and adds one object DM with another object DB.
- Use a friend function to carry out the addition.
- The object that stores the results may be a DM object or DB object, depending on the units in which the results are required.
- The display should be in the format of feet and inches or meters and centimeters depending on the object on display.

**Program:**

```cpp
#include <iostream>
using namespace std;

class DB;

class DM {
    int m;
    int cm;

    friend DM toDM(DM, DB);
    friend DB toDB(DM, DB);

public:
    DM() {}
    DM(int a, int b) : m{a}, cm{b} {}
    
    void print() {
        cout << m << "." << cm << "m" << endl;
    }
};

class DB {
    int ft;
    int in;

    friend DM toDM(DM, DB);
    friend DB toDB(DM, DB);

public:
    DB() {}
    DB(int a, int b) : ft{a}, in{b} {}

    void print() {
        cout << ft << "." << in << "ft" << endl;
    }
};

DM toDM(DM a, DB b) {
    int totalin = b.ft * 12;
    int totalcm = a.cm + totalin * 2.54;

    int m = a.m, cm = a.cm;

    while (totalcm >= 100) {
        m = m + 1;
        totalcm -= 100;
        cm = totalcm;
    }
    return DM(m, cm);
}

DB toDB(DM a, DB b) {
    int totalcm = a.m * 100;
    int totalin = b.in + (totalcm / 2.54);

    int ft = b.ft, in = b.in;

    while (totalin >= 12) {
        ft = ft + 1;
        totalin -= 12;
        in = totalin;
    }
    return DB(ft, in);
}

int main() {
    DM a(5, 3);
    DB b(1, 1);

    DM c = toDM(a, b);
    DB d = toDB(a, b);

    c.print();
    d.print();

    return 0;
}
```

**Output:**

```
5.03m
1.18ft
```

---

### 2. Bank Account Program
Assume that a bank maintains two kinds of accounts for customers: one called a savings account and the other a current account.
- The savings account provides compound interest and withdrawal facilities but not cheque book facility.
- The current account provides cheque book facility but no interest.
- Current account holders should maintain a minimum balance, and if the balance falls below this level, a service charge is imposed.

**Program:**

```cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

class Account {
protected:
    string name;
    int account_no;
    double balance;

public:
    void setAccountDetails(const string& n, int accNo, double bal) {
        name = n;
        account_no = accNo;
        balance = bal;
    }

    void display() {
        cout << "Account Name: " << name << endl;
        cout << "Account Number: " << account_no << endl;
        cout << "Account Balance: " << balance << endl;
    }

    void deposit(double amount) {
        balance += amount;
        cout << "Deposited: " << amount << endl;
        cout << "Updated Balance: " << balance << endl;
    }

    virtual void withdraw(double amount) = 0;
};

class Savings : public Account {
public:
    void interest(double rate, int years) {
        double interestAmount = balance * pow((1 + (rate / 100)), years) - balance;
        balance += interestAmount;
        cout << "Interest added: " << interestAmount << endl;
        cout << "New balance: " << balance << endl;
    }

    void withdraw(double amount) override {
        if (amount <= balance) {
            balance -= amount;
            cout << "Amount withdrawn: " << amount << endl;
            cout << "New balance: " << balance << endl;
        } else {
            cout << "Insufficient balance!" << endl;
        }
    }
};

class Current : public Account {
private:
    double minimumBalance;
    double serviceCharge;

public:
    void setCurrentAccountDetails(double minBalance, double charge) {
        minimumBalance = minBalance;
        serviceCharge = charge;
    }

    void withdraw(double amount) override {
        if (amount <= balance) {
            balance -= amount;
            cout << "Amount withdrawn: " << amount << endl;
            if (balance < minimumBalance) {
                balance -= serviceCharge;
                cout << "Balance below minimum! Service charge imposed: " << serviceCharge << endl;
            }
            cout << "New balance: " << balance << endl;
        } else {
            cout << "Insufficient balance!" << endl;
        }
    }
};

int main() {
    Savings savingsAccount;
    savingsAccount.setAccountDetails("Alice", 101, 5000);
    savingsAccount.display();
    savingsAccount.deposit(2000);
    savingsAccount.interest(5, 2);
    savingsAccount.withdraw(3000);

    cout << endl;

    Current currentAccount;
    currentAccount.setAccountDetails("Bob", 102, 3000);
    currentAccount.setCurrentAccountDetails(2000, 100);
    currentAccount.display();
    currentAccount.deposit(1500);
    currentAccount.withdraw(4000);
    currentAccount.withdraw(500);

    return 0;
}
```

**Output:**

```
Account Name: Alice
Account Number: 101
Account Balance: 5000
Deposited: 2000
Updated Balance: 7000
Interest added: 735.15
New balance: 7735.15
Amount withdrawn: 3000
New balance: 4735.15

Account Name: Bob
Account Number: 102
Account Balance: 3000
Deposited: 1500
Updated Balance: 4500
Amount withdrawn: 4000
New balance: 1500
Balance below minimum! Service charge imposed: 100
New balance: 1400
Amount withdrawn: 500
New balance: 900
```

---

### 3. Educational Institution Employee Database
An educational institution wishes to maintain a database of its employees. The database is divided into several classes as shown in the following hierarchy.

![{EFEB76F2-A318-4BFC-8B3A-87A098A059A3}](https://github.com/user-attachments/assets/1c1e63fc-2cf3-4f46-8b8f-f896793896ab)


**Program:**

```cpp
#include <iostream>
#include <string>
using namespace std;

class Staff {
protected:
    string name;
    int code;

public:
    Staff(string n, int c) : name{n}, code{c} {}

    void display() {
        cout << "Name: " << name << " | Code: " << code << endl;
    }
};

class Teacher : public Staff {
    string subj;

public:
    Teacher(string name, int c, string sub) : Staff(name, c), subj{sub} {}

    void display() {
        Staff::display();
        cout << "Subject: " << subj << endl;
    }
};

class Officer : public Staff {
    string grade;

public:
    Officer(string name, int c, string grade) : Staff(name, c), grade{grade} {}

    void display() {
        Staff::display();
        cout << "Grade: " << grade << endl;
    }
};

class Typist : public Staff {
    int speed;

public:
    Typist(string name, int c, int speed) : Staff(name, c), speed{speed} {}

    void display() {
        Staff::display();
        cout << "Typing Speed: " << speed << " wpm" << endl;
    }
};

class RegularTypist : public Typist {
public:
    RegularTypist(string name, int c, int speed) : Typist(name, c, speed) {}

    void display() {
        Typist::display();
        cout << "Typist Type: Regular" << endl;
    }
};

class CasualTypist : public Typist {
    int wages;

public:
    CasualTypist(string name, int c, int speed, int w) : Typist(name, c, speed), wages{w} {}

    void display() {
        Typist::display();
        cout << "Typist Type: Casual" << " | Daily Wage: " << wages << endl;
    }
};

int main() {
    Teacher t("Mr. Sharma", 101, "Maths");
    RegularTypist rt("Ms. Anjali", 102, 75);
    CasualTypist ct("Mr. Raj", 103, 65, 300);
    Officer o("Ms. Priya", 104, "A");

    cout << "\nTeacher Details:\n";
    t.display();

    cout << "\nRegular Typist Details:\n";
    rt.display();

    cout << "\nCasual Typist Details:\n";
    ct.display();

    cout << "\nOfficer Details:\n";
    o.display();

    return 0;
}
```

**Output:**

```
Teacher Details:
Name: Mr. Sharma | Code: 101
Subject: Maths

Regular Typist Details:
Name: Ms. Anjali | Code: 102
Typing Speed: 75 wpm
Typist Type:

 Regular

Casual Typist Details:
Name: Mr. Raj | Code: 103
Typing Speed: 65 wpm
Typist Type: Casual | Daily Wage: 300

Officer Details:
Name: Ms. Priya | Code: 104
Grade: A
```


### 4.1 Create a base class called `Shape`. Use this class to store two `double` type values that could be used to compute the area of figures. Derive two specific classes called `Triangle` and `Rectangle` from the base `Shape`. Add to the base class a member function `get_data()` to initialize base class data members and another member function `display_area()` to compute and display the area of figures. Make `display_area()` as a virtual function and redefine this function in the derived classes to suit their requirements. Using these three classes, design a program that will accept dimensions of a triangle or a rectangle interactively, and display the area.

### 4.1 Program

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
    double x, y;
public:
    void get_data(double a, double b) {
        x = a;
        y = b;
    }
    virtual void display_area() {
        cout << "Area not defined." << endl;
    }
};

class Rectangle : public Shape {
public:
    void display_area() override {
        cout << "Area of Rectangle: " << x * y << endl;
    }
};

class Triangle : public Shape {
public:
    void display_area() override {
        cout << "Area of Triangle: " << 0.5 * x * y << endl;
    }
};

int main() {
    Shape* shapePtr;
    Rectangle rect;
    Triangle tri;

    // Example usage
    shapePtr = &rect;
    shapePtr->get_data(10, 20);
    shapePtr->display_area();

    shapePtr = &tri;
    shapePtr->get_data(10, 20);
    shapePtr->display_area();

    return 0;
}
```

#### Output:

```
Area of Rectangle: 200
Area of Triangle: 100
```

---

### 4.2 Extend the above program to display the area of circles. This requires the addition of a new derived class `Circle` that computes the area of a circle. Remember, for a circle we need only one value (its radius), but the `get_data()` function in the base class requires two values to be passed.


### 4.2 Program

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
    double x, y;
public:
    void get_data(double a, double b = 0) { // Second argument default to 0 for circles
        x = a;
        y = b;
    }
    virtual void display_area() {
        cout << "Area not defined." << endl;
    }
};

class Rectangle : public Shape {
public:
    void display_area() override {
        cout << "Area of Rectangle: " << x * y << endl;
    }
};

class Triangle : public Shape {
public:
    void display_area() override {
        cout << "Area of Triangle: " << 0.5 * x * y << endl;
    }
};

class Circle : public Shape {
public:
    void display_area() override {
        cout << "Area of Circle: " << 3.14159 * x * x << endl;
    }
};

int main() {
    Shape* shapePtr;
    Rectangle rect;
    Triangle tri;
    Circle circ;

    // Rectangle
    shapePtr = &rect;
    shapePtr->get_data(10, 20);
    shapePtr->display_area();

    // Triangle
    shapePtr = &tri;
    shapePtr->get_data(10, 20);
    shapePtr->display_area();

    // Circle
    shapePtr = &circ;
    shapePtr->get_data(10); // Only radius is needed
    shapePtr->display_area();

    return 0;
}
```

#### Output:

```
Area of Rectangle: 200
Area of Triangle: 100
Area of Circle: 314.159
```

---

### 4.3 Program

```cpp
#include <iostream>
using namespace std;

class Shape {
protected:
    double x, y;
public:
    void get_data(double a, double b = 0) {
        x = a;
        y = b;
    }
    virtual void display_area() {
        cout << "Area not defined." << endl;
    }
};

class Rectangle : public Shape {
public:
    void display_area() override {
        cout << "Area of Rectangle: " << x * y << endl;
    }
};

// Removed display_area() from Triangle class
class Triangle : public Shape {};

class Circle : public Shape {
public:
    void display_area() override {
        cout << "Area of Circle: " << 3.14159 * x * x << endl;
    }
};

int main() {
    Shape* shapePtr;
    Rectangle rect;
    Triangle tri;
    Circle circ;

    // Rectangle
    shapePtr = &rect;
    shapePtr->get_data(10, 20);
    shapePtr->display_area();

    // Triangle
    shapePtr = &tri;
    shapePtr->get_data(10, 20);
    shapePtr->display_area(); // Falls back to base class definition

    // Circle
    shapePtr = &circ;
    shapePtr->get_data(10);
    shapePtr->display_area();

    return 0;
}
```

#### Output:

```
Area of Rectangle: 200
Area not defined.
Area of Circle: 314.159
```

---


# Lab - 7

# Python
<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---

# Python Programs Report

## 1. **Find the Largest Number in a List**

**Problem Statement:**

Write a Python program to find the largest number in a list of numbers.

**Code:**

```python
# Given list of numbers
numbers = [12, 45, 78, 34, 23, 89, 4]

# Finding the largest number using the max() function
largest_number = max(numbers)

# Printing the largest number
print("The largest number is:", largest_number)
```

**Output:**

```
The largest number is: 89
```

---

## 2. **Sort a Tuple in Ascending Order**

**Problem Statement:**

Write a Python program to sort a tuple in ascending order.

**Code:**

```python
# Given tuple
t = (43, 12, 98, 23, 56, 7)

# Sorting the tuple and converting it back to tuple form
sorted_tuple = tuple(sorted(t))

# Printing the sorted tuple
print("The sorted tuple is:", sorted_tuple)
```

**Output:**

```
The sorted tuple is: (7, 12, 23, 43, 56, 98)
```

---

## 3. **Check if a Particular Element is Present in a Set**

**Problem Statement:**

Write a Python program to check if a particular element is present in a set.

**Code:**

```python
# Given set and element to check
s = {23, 45, 67, 89, 12}
element = 45

# Checking if the element is in the set
if element in s:
    print(f"{element} is present in the set.")
else:
    print(f"{element} is not present in the set.")
```

**Output:**

```
45 is present in the set.
```

---

## 4. **Remove a Particular Key-Value Pair from a Dictionary**

**Problem Statement:**

Write a Python program to remove a particular key-value pair from a dictionary.

**Code:**

```python
# Given dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Key to remove
key_to_remove = 'age'

# Removing the key-value pair
if key_to_remove in my_dict:
    del my_dict[key_to_remove]

# Printing the modified dictionary
print("The dictionary after removal is:", my_dict)
```

**Output:**

```
The dictionary after removal is: {'name': 'Alice', 'city': 'New York'}
```

---

## 5. **Find Unique Values of All Keys and Values in a List of Dictionaries**

**Problem Statement:**

Write a Python program that takes a list of dictionaries as input and returns a tuple of the unique values of all the keys and values in the dictionaries.

**Code:**

```python
# List of dictionaries
dicts_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'city': 'New York', 'age': 25},
]

# Collecting unique keys and values
unique_keys = set()
unique_values = set()

# Looping through the list of dictionaries
for d in dicts_list:
    for key, value in d.items():
        unique_keys.add(key)
        unique_values.add(value)

# Creating a tuple of unique keys and values
unique_tuple = (unique_keys, unique_values)

# Printing the result
print("The unique keys and values are:", unique_tuple)
```

**Output:**

```
The unique keys and values are: ({'name', 'city', 'age'}, {'Bob', 'Alice', 'New York', 25, 30})
```

---

# Lab - 8

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---

# Python Programs Report

## 1. **Convert Kilometers to Miles**

**Problem Statement:**

Write a Python program to convert kilometers to miles.

**Code:**

```python
# Given kilometers
kilometers = 10

# Conversion factor
conversion_factor = 0.621371

# Converting kilometers to miles
miles = kilometers * conversion_factor

# Printing the result
print(f"{kilometers} kilometers is equal to {miles} miles.")
```

**Output:**

```
10 kilometers is equal to 6.21371 miles.
```

---

## 2. **Find the Square Root Without Using Built-in Function**

**Problem Statement:**

Write a Python program to find the square root without using a built-in function.

**Code:**

```python
# Given number
num = 16

# Using Newton's method to find the square root
guess = num / 2  # Initial guess
accuracy = 0.000001  # Define the accuracy

while abs(guess * guess - num) > accuracy:
    guess = (guess + num / guess) / 2

# Printing the square root
print(f"The square root of {num} is approximately {guess}.")
```

**Output:**

```
The square root of 16 is approximately 4.0.
```

---

## 3. **Calculate the Area of a Triangle**

**Problem Statement:**

Write a Python program to calculate the area of a triangle.

**Code:**

```python
# Given base and height of the triangle
base = 10
height = 5

# Calculating the area
area = 0.5 * base * height

# Printing the result
print(f"The area of the triangle is {area} square units.")
```

**Output:**

```
The area of the triangle is 25.0 square units.
```

---

## 4. **Swap Two Variables Using a Third Variable**

**Problem Statement:**

Write a Python program to swap two variables using a third variable.

**Code:**

```python
# Given two variables
a = 5
b = 10

# Using a third variable to swap
temp = a
a = b
b = temp

# Printing the swapped values
print(f"After swapping, a = {a} and b = {b}.")
```

**Output:**

```
After swapping, a = 10 and b = 5.
```

---

## 5. **Check if the User is Permitted to Vote**

**Problem Statement:**

Write a Python program to print the message ‘You are permitted to vote’ when the user-entered age is above 17.

**Code:**

```python
# Getting the user's age
age = int(input("Enter your age: "))

# Checking if the user is permitted to vote
if age > 17:
    print("You are permitted to vote.")
else:
    print("You are not permitted to vote.")
```

**Output (example):**

```
Enter your age: 18
You are permitted to vote.
```

---

# Lab - 9

<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: Advance Programming

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

---

# Lab - 9 Report

## 1. **Multiple Function Calls with Compulsory Argument**

**Problem Statement:**

Write a Python program that demonstrates multiple function calls with compulsory arguments.

**Code:**

```python
# Function that prints a message with a name
def greet(name):
    print(f"Hello, {name}! Welcome to the Python programming world.")

# Calling the function multiple times
greet("Alice")
greet("Bob")
greet("Charlie")
```

**Output:**

```
Hello, Alice! Welcome to the Python programming world.
Hello, Bob! Welcome to the Python programming world.
Hello, Charlie! Welcome to the Python programming world.
```

---

## 2. **Function with a Default Argument**

**Problem Statement:**

Write a Python program that demonstrates a function with a default argument.

**Code:**

```python
# Function that prints a message with a default greeting
def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}")

# Calling the function with and without the default argument
greet("Alice")  # Using default message
greet("Bob", "Good morning!")  # Overriding default message
```

**Output:**

```
Hello, Alice! Welcome!
Hello, Bob! Good morning!
```

---

## 3. **Function with a Return Statement**

**Problem Statement:**

Write a Python program that demonstrates a function with a return statement.

**Code:**

```python
# Function that adds two numbers and returns the result
def add_numbers(a, b):
    result = a + b
    return result

# Using the function and storing the result
sum_value = add_numbers(5, 7)

# Printing the result
print(f"The sum of the two numbers is {sum_value}.")
```

**Output:**

```
The sum of the two numbers is 12.
```

---

## 4. **Example of a Function Returning Multiple Values**

**Problem Statement:**

Write a Python program that demonstrates a function returning multiple values.

**Code:**

```python
# Function that returns the sum and product of two numbers
def sum_and_product(a, b):
    sum_value = a + b
    product_value = a * b
    return sum_value, product_value

# Using the function and unpacking the returned values
sum_result, product_result = sum_and_product(4, 6)

# Printing the results
print(f"The sum is {sum_result} and the product is {product_result}.")
```

**Output:**

```
The sum is 10 and the product is 24.
```

---

## 5. **Find the Largest Number Among Three Numbers**

**Problem Statement:**

Write a Python program to find the largest number among three numbers.

**Code:**

```python
# Given three numbers
a = 12
b = 45
c = 32

# Finding the largest number
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

# Printing the largest number
print(f"The largest number is {largest}.")
```

**Output:**

```
The largest number is 45.
```

---

## 6. **Count the Number of Digits in a Number**

**Problem Statement:**

Write a Python program to count the number of digits in a number.

**Code:**

```python
# Given number
num = 12345

# Counting the number of digits
count = len(str(num))

# Printing the result
print(f"The number {num} has {count} digits.")
```

**Output:**

```
The number 12345 has 5 digits.
```

---

## 7. **Count the Number of Digits in a Number Using While Loop (Without Function)**

**Problem Statement:**

Write a Python program to count the number of digits in a number using a while loop (without using a function).

**Code:**

```python
# Given number
num = 123456

# Initialize count
count = 0

# Counting digits using a while loop
while num != 0:
    num = num // 10  # Remove the last digit
    count += 1  # Increment the count

# Printing the result
print(f"The number has {count} digits.")
```

**Output:**

```
The number has 6 digits.
```

---

## 8. **Compute the Factorial of a Number**

**Problem Statement:**

Write a Python program that computes the factorial of the number passed as an argument.

**Code:**

```python
# Given number
num = 5

# Initialize factorial
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

# Printing the result
print(f"The factorial of {num} is {factorial}.")
```

**Output:**

```
The factorial of 5 is 120.
```

## 8. Using else with while loop

```python
numbers = [1, 3, 5, 7, 2, 9, 10, 11]

# Initialize variables
found_even = None
index = 0

# Start a while loop to search for the first non-negative even number
while index < len(numbers):
    if numbers[index] >= 0 and numbers[index] % 2 == 0:
        found_even = numbers[index]
        break  # Exit the loop if a match is found
    index += 1
else:
    print("No non-negative even number found in the list.")

# Check if a non-negative even number was found and print it
if found_even is not None:
    print(f"The first non-negative even number found is: {found_even}")

```

**Output:**

```
The first non-negative even number found is: 2
```

---


