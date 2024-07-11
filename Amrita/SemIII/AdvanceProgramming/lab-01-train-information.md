# Lab-II Web Technology

2. Create html web page for railway information system using imagetag,table and link tag

Make use of marquee tag( to scroll vertically up), image tag, table and link tag for designing your
web page.
•Mention the train name, number, departure and arrival details of all trains inside a table.
•When user clicks on particular train, he/she should be able to see list of all stops with timings
details.
•Mention the food details available in the train


## Homepage

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indian Railway Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e6f7ff;
            background-image: url('https://www.team-bhp.com/forum/attachments/commercial-vehicles/958448d1691959539t-railway-pics-dsc018501.jpg');
            background-size: cover;
            background-position: center;
        }
        .header {
            background-color: #004080;
            color: white;
            text-align: center;
            padding: 20px;
        }
        .navbar {
            background-color: #003366;
            text-align: center;
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            display: inline-block;
        }
        .content {
            padding: 20px;
            text-align: center;
            color: #333;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            margin: 20px;
        }
      
    </style>
</head>
<body>

    <!-- Header Section -->
    <div class="header">
        <h1>Indian Railway Booking</h1>
    </div>

    <!-- Navigation Bar -->
    <div class="navbar">
        <a href="#">Home</a>
        <a href="./Book_tickets.html">Book Tickets</a>
        <a href="./Schedule.html">Schedule</a>
        <a href="./Food.html">Food Information</a>
    </div>

    <!-- Main Content -->
    <div class="content">
        <h2>Book Your Train Tickets</h2>
        <br>
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/4/45/IRCTC_Logo.svg/150px-IRCTC_Logo.svg.png" alt="IRCTC Logo">
        <p>Welcome to the Indian Railway Booking System. Please use the navigation bar to explore our services.</p>
    </div>


</body>
</html>
```
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/cbbe15e7-4d6a-4ecb-a7f8-9a64643545ef)

### Ticket Booking Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Tickets - Indian Railway Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e6f7ff;
            background-image: url('https://www.team-bhp.com/forum/attachments/commercial-vehicles/958448d1691959539t-railway-pics-dsc018501.jpg');
            background-size: cover;
            background-position: center;
        }
        .header {
            background-color: #004080;
            color: white;
            text-align: center;
            padding: 20px;
        }
        .navbar {
            background-color: #003366;
            text-align: center;
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            display: inline-block;
        }
        .booking-form {
            padding: 20px;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            margin: 20px;
            color: #333;
        }
        .booking-form table {Homepage
            margin: auto;
        }
        .booking-form input[type="text"],
        .booking-form input[type="date"],
        .booking-form select {
            padding: 10px;
            margin: 5px;
            width: 200px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .booking-form input[type="submit"] {
            padding: 10px 20px;
            margin-top: 10px;
            background-color: #004080;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .booking-form input[type="submit"]:hover {
            background-color: #003366;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header">
        <h1>Indian Railway Booking</h1>
    </div>

    <!-- Navigation Bar -->
    <div class="navbar">
        <a href="#">Home</a>
        <a href="./Book_tickets.html">Book Tickets</a>
        <a href="./Schedule.html">Schedule</a>
        <a href="./Food.html">Food Information</a>
    </div>

    <!-- Booking Form -->
    <div class="booking-form">
        <h2>Book Your Train Tickets</h2>
        <form>
            <table cellpadding="10">
                <tr>
                    <td><label for="from">From:</label></td>
                    <td><input type="text" id="from" name="from"></td>
                </tr>
                <tr>
                    <td><label for="to">To:</label></td>
                    <td><input type="text" id="to" name="to"></td>
                </tr>
                <tr>
                    <td><label for="date">Date:</label></td>
                    <td><input type="date" id="date" name="date"></td>
                </tr>
                <tr>
                    <td><label for="class">Class:</label></td>
                    <td>
                        <select id="class" name="class">
                            <option value="sleeper">Sleeper</option>
                            <option value="ac">AC</option>
                            <option value="general">General</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" align="center"><input type="submit" value="Book Ticket"></td>
                </tr>
            </table>
        </form>
    </div>
</body>
</html>
```
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/ed5c9545-7845-4213-8d77-dad0ff4610a8)

## Train Information Page
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Train Schedule - Indian Railway Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e6f7ff;
            background-image: url('https://www.team-bhp.com/forum/attachments/commercial-vehicles/958448d1691959539t-railway-pics-dsc018501.jpg');
            background-size: cover;
            background-position: center;
        }
        .header {
            background-color: #004080;
            color: white;
            text-align: center;
            padding: 20px;
        }
        .navbar {
            background-color: #003366;
            text-align: center;
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            display: inline-block;
        }
        .content {
            padding: 20px;
            text-align: center;
            color: #333;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            margin: 20px;
        }
        .train-list {
            list-style-type: none;
            padding: 0;
        }
        .train-list li {
            padding: 10px;
            background-color: #f0f8ff;
            border: 1px solid #ccc;
            margin: 5px 0;
            border-radius: 5px;
        }
        .train-list li a {
            color: #004080;
            text-decoration: none;
            display: block;
        }
        .train-list li a:hover {
            background-color: #cce7ff;
        }
        .train-details {
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header">
        <h1>Indian Railway Booking</h1>
    </div>

    <!-- Navigation Bar -->
    <div class="navbar">
        <a href="#">Home</a>
        <a href="./Book_tickets.html">Book Tickets</a>
        <a href="./Schedule.html">Schedule</a>
        <a href="./Food.html">Food Information</a>
    </div>

    <!-- Main Content -->
    <div class="content">
        <h2>Train Schedule</h2>
        <ul class="train-list">
            <li><a href="#train1">Train 1</a></li>
            <li><a href="#train2">Train 2</a></li>
            <li><a href="#train3">Train 3</a></li>
        </ul>
        <div id="train1" class="train-details">
            <h3>Train 1 Details</h3>
            <p>Start: Station A</p>
            <p>End: Station E</p>
            <p>Stops: Station B, Station C, Station D</p>
        </div>
        <div id="train2" class="train-details">
            <h3>Train 2 Details</h3>
            <p>Start: Station F</p>
            <p>End: Station J</p>
            <p>Stops: Station G, Station H, Station I</p>
        </div>
        <div id="train3" class="train-details">
            <h3>Train 3 Details</h3>
            <p>Start: Station K</p>
            <p>End: Station O</p>
            <p>Stops: Station L, Station M, Station N</p>
        </div>
    </div>
</body>
</html>
```
![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/36494ea5-4813-4210-8a83-2ce1d4cb43fd)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Train Food Menu - Indian Railway Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #e6f7ff;
            background-image: url('https://www.team-bhp.com/forum/attachments/commercial-vehicles/958448d1691959539t-railway-pics-dsc018501.jpg');
            background-size: cover;
            background-position: center;
        }
        .header {
            background-color: #004080;
            color: white;
            text-align: center;
            padding: 20px;
        }
        .navbar {
            background-color: #003366;
            text-align: center;
            padding: 10px 0;
        }
        .navbar a {
            color: white;
            padding: 14px 20px;
            text-decoration: none;
            display: inline-block;
        }
        .content {
            padding: 20px;
            text-align: center;
            color: #333;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            margin: 20px;
        }
        .train-list {
            list-style-type: none;
            padding: 0;
        }
        .train-list li {
            padding: 10px;
            background-color: #f0f8ff;
            border: 1px solid #ccc;
            margin: 5px 0;
            border-radius: 5px;
        }
        .train-list li a {
            color: #004080;
            text-decoration: none;
            display: block;
        }
        .train-list li a:hover {
            background-color: #cce7ff;
        }
        .train-details {
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            margin-top: 20px;
        }
        .food-item {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <div class="header">
        <h1>Indian Railway Booking</h1>
    </div>

    <!-- Navigation Bar -->
    <div class="navbar">
        <a href="index.html">Home</a>
        <a href="Book_tickets.html">Book Tickets</a>
        <a href="train_schedule.html">Schedule</a>
        <a href="food.html">Food Information</a>
    </div>

    <!-- Main Content -->
    <div class="content">
        <h2>Food Menu</h2>
        <ul class="train-list">
            <li><a href="#train1">Train 1</a></li>
            <li><a href="#train2">Train 2</a></li>
            <li><a href="#train3">Train 3</a></li>
        </ul>
        <div id="train1" class="train-details">
            <h3>Train 1 Food Menu</h3>
            <div class="food-item">
                <h4>Breakfast</h4>
                <p>Idli, Vada, Sambar</p>
                <p>Tea, Coffee</p>
            </div>
            <div class="food-item">
                <h4>Lunch</h4>
                <p>Veg Thali: Rice, Dal, Sabzi, Roti, Salad</p>
                <p>Non-Veg Thali: Chicken Curry, Rice, Roti, Salad</p>
            </div>
            <div class="food-item">
                <h4>Dinner</h4>
                <p>Biryani: Veg/Chicken</p>
                <p>Curry: Paneer/Chicken</p>
            </div>
        </div>
        <div id="train2" class="train-details">
            <h3>Train 2 Food Menu</h3>
            <div class="food-item">
                <h4>Breakfast</h4>
                <p>Poori, Bhaji</p>
                <p>Tea, Coffee</p>
            </div>
            <div class="food-item">
                <h4>Lunch</h4>
                <p>South Indian Thali: Rice, Sambar, Rasam, Poriyal, Roti</p>
                <p>Non-Veg Thali: Fish Curry, Rice, Roti, Salad</p>
            </div>
            <div class="food-item">
                <h4>Dinner</h4>
                <p>Fried Rice: Veg/Chicken</p>
                <p>Noodles: Veg/Chicken</p>
            </div>
        </div>
        <div id="train3" class="train-details">
            <h3>Train 3 Food Menu</h3>
            <div class="food-item">
                <h4>Breakfast</h4>
                <p>Uttapam, Chutney</p>
                <p>Tea, Coffee</p>
            </div>
            <div class="food-item">
                <h4>Lunch</h4>
                <p>North Indian Thali: Rice, Dal, Sabzi, Roti, Salad</p>
                <p>Non-Veg Thali: Mutton Curry, Rice, Roti, Salad</p>
            </div>
            <div class="food-item">
                <h4>Dinner</h4>
                <p>Paneer Butter Masala, Naan</p>
                <p>Chicken Tikka Masala, Naan</p>
            </div>
        </div>
    </div>
</body>
</html>


```

![image](https://github.com/ShudarsanRegmi/myDigiNotes/assets/65646203/ca0329c0-1d38-42f3-876c-9493fe0d03d8)
