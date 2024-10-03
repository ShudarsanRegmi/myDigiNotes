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

# Science Exhibition

### Competition Details Page

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Science Exhibition - Competition Details</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Amrita Vishwa Vidyapeetham Science Exhibition</h1>
        <p>Organized by RSTS Science Team</p>
    </header>
    
    <section>
        <h2>Competition Categories</h2>
        <ul>
            <li><strong>Physics:</strong> Projects based on the principles of physics.</li>
            <li><strong>Chemistry:</strong> Innovative chemical experiments and research.</li>
            <li><strong>Biology:</strong> Projects on biology, health, or environment.</li>
            <li><strong>Engineering:</strong> Technological solutions, robotics, and engineering designs.</li>
        </ul>

        <h2>Rules and Guidelines</h2>
        <ol>
            <li>Each team can have up to 3 members.</li>
            <li>Projects should be original and innovative.</li>
            <li>All participants must be students of schools affiliated with Amrita Vishwa Vidyapeetham.</li>
            <li>The competition will be judged by a panel of experts from each field.</li>
            <li>Judging criteria include creativity, innovation, and project presentation.</li>
        </ol>
    </section>
    
    <footer>
        <p>Contact us: scienceexhibition@amrita.edu | Phone: +91 9876543210</p>
    </footer>
</body>
</html>

```

### Output
![{F64B75C0-8E08-4D6A-9A9E-F6E52D27AA5B}](https://github.com/user-attachments/assets/d1b7d7c3-b4c3-4449-a992-298842a9a7b4)

### Events Schedule

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Science Exhibition - Event Schedule</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Amrita Vishwa Vidyapeetham Science Exhibition</h1>
        <p>Organized by RSTS Science Team</p>
    </header>
    
    <section>
        <h2>Event Schedule</h2>
        <table>
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Event</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>9:00 AM - 10:00 AM</td>
                    <td>Opening Ceremony</td>
                    <td>Main Auditorium</td>
                </tr>
                <tr>
                    <td>10:30 AM - 12:30 PM</td>
                    <td>Project Presentations - Physics & Chemistry</td>
                    <td>Room 101 & 102</td>
                </tr>
                <tr>
                    <td>1:00 PM - 2:00 PM</td>
                    <td>Lunch Break</td>
                    <td>Cafeteria</td>
                </tr>
                <tr>
                    <td>2:30 PM - 4:30 PM</td>
                    <td>Project Presentations - Biology & Engineering</td>
                    <td>Room 103 & 104</td>
                </tr>
                <tr>
                    <td>5:00 PM - 6:00 PM</td>
                    <td>Award Ceremony</td>
                    <td>Main Auditorium</td>
                </tr>
            </tbody>
        </table>
    </section>
    
    <footer>
        <p>Contact us: scienceexhibition@amrita.edu | Phone: +91 9876543210</p>
    </footer>
</body>
</html>

```
### Output
![{2F853291-A7E5-4898-9736-6D0EE0BB21DC}](https://github.com/user-attachments/assets/d60fda8a-83aa-4fb3-8295-a811d0b19240)


### Registration

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Science Exhibition - Registration</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Amrita Vishwa Vidyapeetham Science Exhibition</h1>
        <p>Organized by RSTS Science Team</p>
    </header>
    
    <section>
        <h2>Student Registration Form</h2>
        <form action="/submit_registration" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br>

            <label for="school">School/Institution:</label>
            <input type="text" id="school" name="school" required><br>

            <label for="grade">Grade/Year:</label>
            <input type="text" id="grade" name="grade" required><br>

            <label for="project-title">Project Title:</label>
            <input type="text" id="project-title" name="project-title" required><br>

            <label for="category">Select Category:</label>
            <select id="category" name="category" required>
                <option value="Physics">Physics</option>
                <option value="Chemistry">Chemistry</option>
                <option value="Biology">Biology</option>
                <option value="Engineering">Engineering</option>
            </select><br>

            <label for="description">Project Description:</label><br>
            <textarea id="description" name="description" rows="5" required></textarea><br>

            <button type="submit">Submit</button>
        </form>
    </section>
    
    <footer>
        <p>Contact us: scienceexhibition@amrita.edu | Phone: +91 9876543210</p>
    </footer>
</body>
</html>

```

### Output
![{92BAEA66-1DF9-4DAB-8D8F-1E9ACB00A9B6}](https://github.com/user-attachments/assets/5b3731c9-1f0d-419e-95f4-aa1c1db69068)


### Stylesheet

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background-color: #2c3e50;
    color: white;
    padding: 20px;
    text-align: center;
}

h1 {
    margin: 0;
}

h2 {
    margin-top: 20px;
}

section {
    padding: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid #ddd;
}

th, td {
    padding: 12px;
    text-align: left;
}

footer {
    background-color: #2c3e50;
    color: white;
    text-align: center;
    padding: 10px;
    position: absolute;
    width: 100%;
    bottom: 0;
}

```
