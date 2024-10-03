
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


# Calculator and odd even checker

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Calculator and Odd/Even Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1, h2 {
            text-align: center;
        }
        .container {
            max-width: 400px;
            margin: 0 auto;
        }
        .input-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="number"], input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px;
            width: 100%;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            margin-bottom: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        p {
            text-align: center;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>Simple Calculator & Odd/Even Checker</h1>
    
    <div class="container">
        <!-- Simple Calculator Section -->
        <h2>Calculator</h2>
        <div class="input-group">
            <label for="num1">Enter First Number:</label>
            <input type="number" id="num1" placeholder="Enter first number">
        </div>
        <div class="input-group">
            <label for="num2">Enter Second Number:</label>
            <input type="number" id="num2" placeholder="Enter second number">
        </div>
        <div class="input-group">
            <label for="operation">Select Operation:</label>
            <select id="operation">
                <option value="add">Add (+)</option>
                <option value="subtract">Subtract (-)</option>
                <option value="multiply">Multiply (*)</option>
                <option value="divide">Divide (/)</option>
            </select>
        </div>
        <button onclick="calculate()">Calculate</button>
        <p id="calcResult"></p>

        <!-- Odd or Even Checker Section -->
        <h2>Odd or Even Checker</h2>
        <div class="input-group">
            <label for="numCheck">Enter a Number:</label>
            <input type="number" id="numCheck" placeholder="Enter a number">
        </div>
        <button onclick="checkOddOrEven()">Check Odd/Even</button>
        <p id="oddEvenResult"></p>
    </div>

    <script>
        // Simple Calculator Function
        function calculate() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const operation = document.getElementById('operation').value;

            if (isNaN(num1) || isNaN(num2)) {
                document.getElementById('calcResult').innerText = 'Please enter valid numbers.';
                return;
            }

            let result;
            switch (operation) {
                case 'add':
                    result = num1 + num2;
                    break;
                case 'subtract':
                    result = num1 - num2;
                    break;
                case 'multiply':
                    result = num1 * num2;
                    break;
                case 'divide':
                    if (num2 === 0) {
                        document.getElementById('calcResult').innerText = 'Cannot divide by zero.';
                        return;
                    }
                    result = num1 / num2;
                    break;
                default:
                    document.getElementById('calcResult').innerText = 'Invalid operation selected.';
                    return;
            }

            document.getElementById('calcResult').innerText = `Result: ${result}`;
        }

        // Odd or Even Checker Function
        function checkOddOrEven() {
            const num = parseInt(document.getElementById('numCheck').value);

            if (isNaN(num)) {
                document.getElementById('oddEvenResult').innerText = 'Please enter a valid number.';
                return;
            }

            if (num % 2 === 0) {
                document.getElementById('oddEvenResult').innerText = `${num} is an Even number.`;
            } else {
                document.getElementById('oddEvenResult').innerText = `${num} is an Odd number.`;
            }
        }
    </script>

</body>
</html>


```


### Output

![{DA719D71-1682-42DA-8DB5-ABD3F4AB97A5}](https://github.com/user-attachments/assets/6eaf60fa-6543-4b16-8e00-5aed2a6de083)


