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
