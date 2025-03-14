# Creating CrudApp : mysql database


**Application Properties**
```
spring.datasource.url=jdbc:mysql://localhost:3306/crudapp
spring.datasource.username=user3
spring.datasource.password=user3
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```


**Directory Structure**
![image](https://github.com/user-attachments/assets/4721064e-6342-4c60-80f9-7ff9c17ef117)
![image](https://github.com/user-attachments/assets/0da2d2fd-0814-47ed-8902-34cda6177ef0)


```
.
├── java
│   └── com
│       └── shud
│           └── crudapp
│               ├── ApiController.java
│               ├── controller
│               │   └── StudentController.java
│               ├── CrudappApplication.java
│               ├── model
│               │   └── Student.java
│               ├── PagesController.java
│               ├── repository
│               │   └── StudentRepository.java
│               └── service
│                   └── StudentService.java
└── resources
    ├── application.properties
    ├── static
    └── templates
        ├── index.html
        ├── student-form.html
        └── students.html

11 directories, 11 files

```




**StudentController.java**

```java
package com.shud.crudapp.controller;

import com.shud.crudapp.service.StudentService;
import com.shud.crudapp.model.Student;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@Controller
@RequestMapping("/students")
public class StudentController {
    @Autowired
    private StudentService studentService;

    @GetMapping
    public String listStudents(Model model) {
        List<Student> students = studentService.getAllStudents();
        model.addAttribute("students", students);
        return "students";
    }

    @GetMapping("/add")
    public String showAddForm(Model model) {
        model.addAttribute("student", new Student());
        return "student-form";
    }

    @PostMapping("/save")
    public String saveStudent(@ModelAttribute Student student) {
        studentService.saveStudent(student);
        return "redirect:/students";
    }

    @GetMapping("/delete/{id}")
    public String deleteStudent(@PathVariable Long id) {
        studentService.deleteStudent(id);
        return "redirect:/students";
    }
}

```


**Student Modeo**
```java
package com.shud.crudapp.model;


import jakarta.persistence.*;

@Entity
public class Student {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    private String email;

    // Constructors
    public Student() {}

    public Student(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
```

```java

package com.shud.crudapp.repository;

import com.shud.crudapp.model.Student;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
}


    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}
```

**Repository**

```java
package com.shud.crudapp.repository;

import com.shud.crudapp.model.Student;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {
}

```

**StudentService**

```java
package com.shud.crudapp.service;


import com.shud.crudapp.model.Student;
import com.shud.crudapp.repository.StudentRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;


@Service
public class StudentService {
    @Autowired
    private StudentRepository studentRepository;

    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }

    public Student getStudentById(Long id) {
        return studentRepository.findById(id).orElse(null);
    }

    public void saveStudent(Student student) {
        studentRepository.save(student);
    }

    public void deleteStudent(Long id) {
        studentRepository.deleteById(id);
    }
}
```

**ApiController**
```java
// just for checking whether restapii is working or not
package com.shud.crudapp;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ApiController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World";
    }
}
```

**PagesController**
```java
package com.shud.crudapp;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class PagesController {
    @GetMapping("/")
    public String index() {
        return "index";
    }
}
```

---
### Templates

**index.html**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Document</title>
</head>
<body>
<h1>Welcome to a simple crud app</h1>
</body>
</html>
```
**student-form.html**

```java
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Add Student</title>
</head>
<body>
<h2>Add New Student</h2>
<form th:action="@{/students/save}" th:object="${student}" method="post">
    <label>Name:</label>
    <input type="text" th:field="*{name}" required>
    <label>Email:</label>
    <input type="email" th:field="*{email}" required>
    <button type="submit">Save</button>
</form>
</body>
</html>
```

**students.html**
```java
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Student List</title>
</head>
<body>
<h2>Student List</h2>
<a href="/students/add">Add Student</a>
<table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
        <th>Actions</th>
    </tr>
    <tr th:each="student : ${students}">
        <td th:text="${student.id}"></td>
        <td th:text="${student.name}"></td>
        <td th:text="${student.email}"></td>
        <td>
            <a th:href="@{/students/delete/{id}(id=${student.id})}">Delete</a>
        </td>
    </tr>
</table>
</body>
</html>
```

---

## Adding new functionality of updating user


### Adding the controller
`StudentController.java`
```java
@GetMapping("/edit/{id}")
public String showEditForm(@PathVariable Long id, Model model) {
    Student student = studentService.getStudentById(id);
    model.addAttribute("student", student);
    return "student-form";
}
```

### Updating the logic on student-form.html
`student-form.html`

```java
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Student Form</title>
</head>
<body>
    <h2 th:text="${student.id} ? 'Edit Student' : 'Add Student'"></h2>
    <form th:action="@{/students/save}" th:object="${student}" method="post">
        <input type="hidden" th:field="*{id}">  <!-- Hidden field for updating -->
        
        <label>Name:</label>
        <input type="text" th:field="*{name}" required>
        
        <label>Email:</label>
        <input type="email" th:field="*{email}" required>

        <button type="submit">Save</button>
    </form>
</body>
</html>
```

### Adding column for edit in the listing table

`students.html`

```html
<td>
    <a th:href="@{/students/edit/{id}(id=${student.id})}">Edit</a>
    <a th:href="@{/students/delete/{id}(id=${student.id})}">Delete</a>
</td>
```


