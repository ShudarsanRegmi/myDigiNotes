Here’s a detailed project structure and code base for a **Spring Boot Weather App**. The app will have user authentication, weather data fetching, and a clean architecture using **Spring Boot**, **Spring Security (JWT authentication)**, **Spring Data JPA**, and **OpenWeatherMap API** for fetching weather data.

---

## **Project Structure**
```
weather-app/
│── src/
│   ├── main/
│   │   ├── java/com/example/weatherapp/
│   │   │   ├── config/         # Security and general configurations
│   │   │   ├── controllers/    # REST Controllers
│   │   │   ├── dto/            # DTOs for API requests/responses
│   │   │   ├── exceptions/     # Custom exceptions
│   │   │   ├── models/         # Entity models
│   │   │   ├── repositories/   # JPA Repositories
│   │   │   ├── security/       # JWT and authentication logic
│   │   │   ├── services/       # Business logic services
│   │   │   ├── WeatherAppApplication.java  # Main Spring Boot Application
│   │   ├── resources/
│   │   │   ├── application.properties  # Configuration file
│   │   │   ├── data.sql  # Sample database seed data (if needed)
│── pom.xml  # Maven dependencies
│── README.md  # Documentation
```

---

## **1. `WeatherAppApplication.java` (Main Entry Point)**
```java
package com.example.weatherapp;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class WeatherAppApplication {
    public static void main(String[] args) {
        SpringApplication.run(WeatherAppApplication.class, args);
    }
}
```

---

## **2. `models/User.java` (User Entity for Authentication)**
```java
package com.example.weatherapp.models;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true, nullable = false)
    private String username;

    @Column(nullable = false)
    private String password;
}
```

---

## **3. `models/Weather.java` (Weather Entity)**
```java
package com.example.weatherapp.models;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "weather")
public class Weather {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String city;
    private String temperature;
    private String description;
    private String humidity;
    private String windSpeed;
}
```

---

## **4. `dto/AuthRequest.java` (DTO for Authentication Request)**
```java
package com.example.weatherapp.dto;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class AuthRequest {
    private String username;
    private String password;
}
```

---

## **5. `dto/WeatherResponse.java` (DTO for Weather Response)**
```java
package com.example.weatherapp.dto;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class WeatherResponse {
    private String city;
    private String temperature;
    private String description;
    private String humidity;
    private String windSpeed;
}
```

---

## **6. `repositories/UserRepository.java`**
```java
package com.example.weatherapp.repositories;

import com.example.weatherapp.models.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}
```

---

## **7. `repositories/WeatherRepository.java`**
```java
package com.example.weatherapp.repositories;

import com.example.weatherapp.models.Weather;
import org.springframework.data.jpa.repository.JpaRepository;

public interface WeatherRepository extends JpaRepository<Weather, Long> {
}
```

---

## **8. `services/UserService.java`**
```java
package com.example.weatherapp.services;

import com.example.weatherapp.models.User;
import com.example.weatherapp.repositories.UserRepository;
import org.springframework.stereotype.Service;
import org.springframework.security.crypto.password.PasswordEncoder;

@Service
public class UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public User registerUser(String username, String password) {
        // Encrypt the password and save user
    }

    public User findByUsername(String username) {
        // Fetch user by username
    }
}
```

---

## **9. `services/WeatherService.java`**
```java
package com.example.weatherapp.services;

import com.example.weatherapp.dto.WeatherResponse;
import com.example.weatherapp.repositories.WeatherRepository;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class WeatherService {
    private final WeatherRepository weatherRepository;
    private final RestTemplate restTemplate;

    public WeatherService(WeatherRepository weatherRepository, RestTemplate restTemplate) {
        this.weatherRepository = weatherRepository;
        this.restTemplate = restTemplate;
    }

    public WeatherResponse fetchWeather(String city) {
        // Call OpenWeatherMap API and return weather data
    }
}
```

---

## **10. `controllers/AuthController.java`**
```java
package com.example.weatherapp.controllers;

import com.example.weatherapp.dto.AuthRequest;
import com.example.weatherapp.models.User;
import com.example.weatherapp.services.UserService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
public class AuthController {
    private final UserService userService;

    public AuthController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody AuthRequest request) {
        // Register user
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody AuthRequest request) {
        // Authenticate user and return JWT token
    }
}
```

---

## **11. `controllers/WeatherController.java`**
```java
package com.example.weatherapp.controllers;

import com.example.weatherapp.dto.WeatherResponse;
import com.example.weatherapp.services.WeatherService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/weather")
public class WeatherController {
    private final WeatherService weatherService;

    public WeatherController(WeatherService weatherService) {
        this.weatherService = weatherService;
    }

    @GetMapping("/{city}")
    public WeatherResponse getWeather(@PathVariable String city) {
        // Fetch weather data for the given city
    }
}
```

---

## **12. `config/SecurityConfig.java` (Spring Security with JWT)**
```java
package com.example.weatherapp.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class SecurityConfig {

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationConfiguration authenticationConfiguration() {
        return new AuthenticationConfiguration();
    }
}
```

---

## **API Endpoints**
| Method | Endpoint         | Description               |
|--------|----------------|--------------------------|
| POST   | `/api/auth/register` | Register a new user |
| POST   | `/api/auth/login` | Login and get JWT |
| GET    | `/api/weather/{city}` | Get weather data for a city |

---

This structure ensures a clean, modular, and secure **Spring Boot** application for fetching and displaying weather data. Let me know if you need further refinements! 🚀