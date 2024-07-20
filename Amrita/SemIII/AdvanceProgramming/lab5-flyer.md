

## Task 5: The goal is to create a quick short brief webpage using HTML and CSS tags. It’s kind of
flyer

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amrita Vishwa Vidyapeetham Tech Hackathon</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 1200px;
            padding: 40px;
            text-align: center;
        }
        header {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 30px;
        }
        header img {
            width: 100px;
            height: auto;
            margin-right: 20px;
        }
        h1 {
            font-size: 2.5em;
            color: #333;
            margin: 0;
        }
        main {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            align-items: center;
        }
        .image-container {
            flex: 1 1 40%;
            margin: 10px;
        }
        .image-container img {
            width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .content {
            flex: 1 1 40%;
            margin: 10px;
            text-align: left;
        }
        h2 {
            font-size: 2em;
            color: #007bff;
            margin-bottom: 15px;
        }
        p {
            font-size: 1.2em;
            line-height: 1.5;
            color: #666;
            margin-bottom: 20px;
        }
        ul {
            list-style: none;
            padding: 0;
            margin: 0 0 20px 0;
            color: #666;
        }
        ul li {
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        a {
            display: inline-block;
            padding: 15px 30px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1.2em;
            transition: background-color 0.3s ease;
        }
        a:hover {
            background-color: #0056b3;
        }
        footer {
            margin-top: 30px;
            color: #999;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <img src="https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg" alt="Amrita Vishwa Vidyapeetham Logo">
            <h1>Amrita Vishwa Vidyapeetham Tech Hackathon</h1>
        </header>
        <main>
            <div class="image-container">
                <img src="https://webfiles.amrita.edu/2021/08/gQ7zzSDb-AWS-Graviton-Hackathon-2021-%E2%80%93-Winners.jpg" alt="People coding at a hackathon">
            </div>
            <div class="content">
                <h2>Calling all tech innovators!</h2>
                <p>Amrita Vishwa Vidyapeetham presents its annual Tech Hackathon, a thrilling weekend event where coders, designers, and problem-solvers come together to create groundbreaking tech solutions. Put your skills to the test, collaborate with brilliant minds, and compete for exciting prizes!</p>
                <ul>
                    <li><strong>Theme:</strong> Sustainable Cities</li>
                    <li><strong>Dates:</strong> July 25-26, 2024</li>
                    <li><strong>Venue:</strong> Amrita Vishwa Vidyapeetham, Chennai Campus</li>
                    <li><strong>Prizes:</strong> Cash prizes, Internship opportunities, Mentorship</li>
                </ul>
                <a href="#">Register Now!</a>
            </div>
        </main>
        <footer>
            <p>&copy; Amrita Vishwa Vidyapeetham 2024</p>
        </footer>
    </div>
</body>
</html>
```
## Output
![image](https://github.com/user-attachments/assets/dd6d5044-5fc2-47a2-be95-303fa38256b0)

## Result: Flyer was made using HTML and CSS
