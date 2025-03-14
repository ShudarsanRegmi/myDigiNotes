# Spring Boot Basics
![image](https://github.com/user-attachments/assets/4e6fc473-4c93-4bc1-b268-77e1c96581de)

**Running the first app**
![image](https://github.com/user-attachments/assets/fbe70029-9b28-4575-ae27-68291de1783b)


**The Main Entry point remains same**

```java
package com.shud.restapi2;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Restapi2Application {

    public static void main(String[] args) {
        SpringApplication.run(Restapi2Application.class, args);
    }

}
```
![image](https://github.com/user-attachments/assets/b0a7d777-811e-4e2e-ba49-aa87cc480573)


## To Create a simple endpoint

```java
@RestController
@RequestMapping("/api")
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Spring Boot Hello";
    }
    
}
```

## To return a json response
```java
  @GetMapping("/json")
    public Map<String, String> getJsonResponse() {
        Map<String, String> response = new HashMap<>();
        response.put("message", "Hello, this is a JSON response!");
        response.put("status", "success");
        return response;
    }
```

## Basics of using thyemleaf templates

By default, Thymeleaf will look for HTML files inside the `src/main/resources/templates/` folder.

In order to add thyemleaf if not already in meaven project them following should be added under dependencies tag in `pom.xml`

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```


### Creating the fist thyemleaf page
![image](https://github.com/user-attachments/assets/1a0a462a-1735-44d6-99e4-d1f34f930c38)

**Create the class and controller**
```java
package com.shud.libapp3;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    @GetMapping("/home")
    public String home() {
        return "home"; // refers to home.html under  resources/templates/home.html
    }
}

```

**A basic thyemleaf template**
```java
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Thymeleaf Test</title>
</head>
<body>
<h1>Hello, Thymeleaf is Working!</h1>
</body>
</html>
```
