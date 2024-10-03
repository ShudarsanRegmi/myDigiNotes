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

--

# Event Handilng in JavaScript

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Event Handling</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        .event-box {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }
        .event-item {
            padding: 20px;
            background-color: lightgray;
            border: 2px solid black;
            width: 150px;
            text-align: center;
            cursor: pointer;
        }
        .event-item:hover {
            background-color: lightblue;
        }
        p {
            text-align: center;
        }
    </style>
</head>
<body>

    <h1>JavaScript Event Handling</h1>

    <!-- Event-Handling Buttons and Divs -->
    <div class="event-box">
        <!-- OnClick Event -->
        <div class="event-item" onclick="handleClick()">
            Click Me!
        </div>
        <!-- OnMouseDown Event -->
        <div class="event-item" onmousedown="handleMouseDown()">
            Mouse Down
        </div>
        <!-- OnMouseUp Event -->
        <div class="event-item" onmouseup="handleMouseUp()">
            Mouse Up
        </div>
        <!-- OnDoubleClick Event -->
        <div class="event-item" ondblclick="handleDoubleClick()">
            Double Click Me!
        </div>
    </div>

    <p id="resultMessage">Interact with the elements to see event handling in action!</p>

    <script>
        // Event handling functions
        function handleClick() {
            document.getElementById('resultMessage').innerText = 'You clicked the "Click Me!" box.';
        }

        function handleMouseDown() {
            document.getElementById('resultMessage').innerText = 'You pressed down the mouse on the "Mouse Down" box.';
        }

        function handleMouseUp() {
            document.getElementById('resultMessage').innerText = 'You released the mouse button on the "Mouse Up" box.';
        }

        function handleDoubleClick() {
            document.getElementById('resultMessage').innerText = 'You double-clicked the "Double Click Me!" box.';
        }
    </script>

</body>
</html>

```

### Output

![{F5A7A250-8436-4ED1-98E3-6AA3E90E3DC0}](https://github.com/user-attachments/assets/cc8a6d3e-b9df-42bd-8dcb-1bc51d3ff2b0)
