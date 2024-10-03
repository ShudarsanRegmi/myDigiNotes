<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---

### Subject: User Interface Design (UID)

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

# Form Validation Using JavaScript

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Validation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            text-align: center;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
        }
        .input-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="email"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px;
            width: 100%;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            margin-bottom: 10px;
        }
        .success {
            color: green;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

    <h1>Form Validation</h1>

    <div class="container">
        <!-- Form Section -->
        <form id="registrationForm" onsubmit="return validateForm()">
            <!-- Email Input -->
            <div class="input-group">
                <label for="email">Email:</label>
                <input type="email" id="email" placeholder="Enter your email">
                <span class="error" id="emailError"></span>
            </div>

            <!-- Password Input -->
            <div class="input-group">
                <label for="password">Password:</label>
                <input type="password" id="password" placeholder="Enter your password">
                <span class="error" id="passwordError"></span>
            </div>

            <!-- Zipcode Input -->
            <div class="input-group">
                <label for="zipcode">Zip Code:</label>
                <input type="text" id="zipcode" placeholder="Enter your zip code">
                <span class="error" id="zipcodeError"></span>
            </div>

            <button type="submit">Submit</button>
            <p id="formResult"></p>
        </form>
    </div>

    <script>
        // Function to validate the form
        function validateForm() {
            // Clear previous error messages
            document.getElementById('emailError').innerText = '';
            document.getElementById('passwordError').innerText = '';
            document.getElementById('zipcodeError').innerText = '';
            document.getElementById('formResult').innerText = '';

            let isValid = true;

            // Validate Email
            const email = document.getElementById('email').value;
            const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailPattern.test(email)) {
                document.getElementById('emailError').innerText = 'Please enter a valid email address.';
                isValid = false;
            }

            // Validate Password (at least 8 characters, includes letters and numbers)
            const password = document.getElementById('password').value;
            const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
            if (!passwordPattern.test(password)) {
                document.getElementById('passwordError').innerText = 'Password must be at least 8 characters long and include both letters and numbers.';
                isValid = false;
            }

            // Validate Zip Code (5 digits)
            const zipcode = document.getElementById('zipcode').value;
            const zipcodePattern = /^\d{5}$/;
            if (!zipcodePattern.test(zipcode)) {
                document.getElementById('zipcodeError').innerText = 'Zip code must be exactly 5 digits.';
                isValid = false;
            }

            // If all fields are valid
            if (isValid) {
                document.getElementById('formResult').innerText = 'Form submitted successfully!';
                document.getElementById('formResult').classList.add('success');
                return true; // Form is submitted
            } else {
                document.getElementById('formResult').innerText = 'Form submission failed. Please fix the errors above.';
                document.getElementById('formResult').classList.add('error');
                return false; // Prevent form submission
            }
        }
    </script>

</body>
</html>

```

### Output

![{F163C8F8-09D3-4E40-86C0-FA224E8A70C6}](https://github.com/user-attachments/assets/f8754a13-a25d-4c6a-ba57-670dad0b6920)
