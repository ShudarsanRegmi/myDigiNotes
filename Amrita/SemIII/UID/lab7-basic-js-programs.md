


### Basic Js Programs

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Programs</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        .program {
            margin-bottom: 30px;
        }
        label {
            display: block;
            margin-bottom: 10px;
            font-weight: bold;
        }
        input[type="text"], input[type="number"] {
            padding: 8px;
            width: 100%;
            margin-bottom: 20px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        p {
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <h1>JavaScript Programs</h1>

    <!-- Program 1: Welcome Message -->
    <div class="program">
        <h2>Program 1: Welcome Message</h2>
        <label for="name">Enter your name:</label>
        <input type="text" id="name" placeholder="Enter your name">
        <button onclick="welcomeUser()">Submit</button>
        <p id="welcomeMessage"></p>
    </div>

    <!-- Program 2: Reverse String -->
    <div class="program">
        <h2>Program 2: Reverse String</h2>
        <label for="string">Enter a string:</label>
        <input type="text" id="string" placeholder="Enter a string">
        <button onclick="reverseString()">Reverse</button>
        <p id="reverseResult"></p>
    </div>

    <!-- Program 3: Add Numbers -->
    <div class="program">
        <h2>Program 3: Add Numbers</h2>
        <label for="floatNumber">Enter a floating point number:</label>
        <input type="number" step="any" id="floatNumber" placeholder="Enter a floating number">
        <label for="intNumber">Enter an integer number:</label>
        <input type="number" id="intNumber" placeholder="Enter an integer">
        <button onclick="addNumbers()">Add</button>
        <p id="additionResult"></p>
    </div>

    <!-- Program 4: Multiplication Table -->
    <div class="program">
        <h2>Program 4: Multiplication Table</h2>
        <label for="tableNumber">Enter a number:</label>
        <input type="number" id="tableNumber" placeholder="Enter a number">
        <button onclick="generateTable()">Generate Table</button>
        <p id="multiplicationTable"></p>
    </div>

    <script>
        // Program 1: Welcome message
        function welcomeUser() {
            const name = document.getElementById('name').value;
            if (name) {
                document.getElementById('welcomeMessage').innerText = `Welcome, ${name}!`;
            } else {
                document.getElementById('welcomeMessage').innerText = 'Please enter a valid name.';
            }
        }

        // Program 2: Reverse string
        function reverseString() {
            const str = document.getElementById('string').value;
            if (str) {
                const reversedStr = str.split('').reverse().join('');
                document.getElementById('reverseResult').innerText = `Reversed String: ${reversedStr}`;
            } else {
                document.getElementById('reverseResult').innerText = 'Please enter a valid string.';
            }
        }

        // Program 3: Add floating point and integer numbers
        function addNumbers() {
            const floatNumber = parseFloat(document.getElementById('floatNumber').value);
            const intNumber = parseInt(document.getElementById('intNumber').value);

            if (!isNaN(floatNumber) && !isNaN(intNumber)) {
                const sum = floatNumber + intNumber;
                document.getElementById('additionResult').innerText = `Sum: ${sum}`;
            } else {
                document.getElementById('additionResult').innerText = 'Please enter valid numbers.';
            }
        }

        // Program 4: Multiplication Table
        function generateTable() {
            const num = parseInt(document.getElementById('tableNumber').value);
            if (!isNaN(num)) {
                let table = `Multiplication Table of ${num}: \n`;
                for (let i = 1; i <= 10; i++) {
                    table += `${num} x ${i} = ${num * i}\n`;
                }
                document.getElementById('multiplicationTable').innerText = table;
            } else {
                document.getElementById('multiplicationTable').innerText = 'Please enter a valid number.';
            }
        }
    </script>

</body>
</html>

```

### Output

![screencapture-127-0-0-1-5500-lab7-prog-html-2024-10-03-07_18_51](https://github.com/user-attachments/assets/d3cb70ee-1e67-4a6d-9f22-3ab44ca6ef9b)
