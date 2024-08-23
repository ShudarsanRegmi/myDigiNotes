<div align="center">

![Amrita Vishwa Vidyapeetham Logo](https://webfiles.amrita.edu/2024/04/WhQq1FiB-amrita-vishwa-vidyapeetham-university-logo-colored-version.svg)

# Amrita Vishwa Vidyapeetham
## Chennai Campus
337/1A, Vengal Village,  
Thiruvallur Taluk & District – 601 103,  
Tamil Nadu, India

---
![image](https://github.com/user-attachments/assets/92efd67d-337b-49b0-b213-de61f40a8c64)


### Subject: User Interface Design (UID)

**Submitted By:** Shudarsan Regmi  
**Roll No.:** CH.SC.U4CYS23055

</div>

## UID Lab - 3 Tourist Information Webpage

```
• Design a tourist information webpage implementing image hotspot to get useful information
about the countries.
• Your webpage should allow the user to select the favorite country from the list box. After
selecting, new page should be opened in another tab displaying the country map.
• Implement image hot spot for the country map showing tourist place details for at least 3
states.
• Make sure all links are opened in new tab.
• You can use additional html tags to make your web page more attractive
```


## Homepage
![image](https://github.com/user-attachments/assets/5071c0f7-2c26-495a-936e-759e4e5ef845)
![image](https://github.com/user-attachments/assets/33ebdaa5-a849-4a47-ab69-06a7e6151133)

**./index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discover Nepal</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Discover Nepal</h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Popular Destinations</a></li>
                <li><a href="#">Culture</a></li>
                <li><a href="#">Travel Tips</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <img src="./images/nepal-hero.jpg" alt="Beautiful view of Nepal" class="heroImg">
            <div class="hero-text">
                <h2>Explore the beauty of Nepal</h2>
                <p>Your guide to the best spots in Nepal</p>
            </div>
        </section>
        <section class="cards">
            <h2>Popular Tourism Spots</h2>
            <div class="card-container">
                <div class="card">
                    <a href="./everest.html">
                        <img src="./images/ev.jpg" alt="Mount Everest">
                    </a>
                    <div class="card-text">
                        <h3>Mount Everest</h3>
                        <a href="./everest.html">Explore More</a>
                    </div>
                </div>
                <div class="card">
                    <a href="./pokhara.html">
                        <img src="./images/talbarahi.jpg" alt="Pokhara">
                    </a>
                    <div class="card-text">
                        <h3>Pokhara</h3>
                        <a href="pokhara.html">Explore More</a>
                    </div>
                </div>
                <div class="card">
                    <a href="./kathmandu.html">
                        <img src="./images/ktm.jpg" alt="Kathmandu">
                    </a>
                    <div class="card-text">
                        <h3>Kathmandu</h3>
                        <a href="kathmandu.html">Explore More</a>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Discover Nepal. All rights reserved.</p>
    </footer>
</body>
</html>
```
## After selecting a place(say Mout Everest) from index.html

![image](https://github.com/user-attachments/assets/78c8c75f-d4b2-4807-b158-5fb42cf8a755)
![image](https://github.com/user-attachments/assets/ab7bec10-5d9a-4160-b73b-05b109bddcfd)

**./mountain.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mount Everest - Discover Nepal</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Mount Everest</h1>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="#">Popular Destinations</a></li>
                <li><a href="#">Culture</a></li>
                <li><a href="#">Travel Tips</a></li>
                <li><a href="#">Contact Us</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <img src="./images/ev.jpg" alt="Mount Everest" class="heroImg">
            <div class="hero-text">
                <h2>Welcome to Mount Everest</h2>
                <p>Explore the adventure capital of Nepal with paragliding, boating, and trekking</p>
            </div>
        </section>
        <section class="details">
            <h2>Accommodations in Mount Everest Area</h2>
            <div class="card-container">
                <div class="card">
                    <a href="./"></a>
                    <img src="./images/heview.jpg" alt="Hotel Example 1">
                    <div class="card-text">
                        <h3>Hotel Everest View</h3>
                        <p>Contact: +977-123-4567</p>
                    </div>
                </div>
                <div class="card">
                    <img src="./images/hotel-namche.jpg" alt="Hotel Example 2">
                    <div class="card-text">
                        <h3>Namche Lodge</h3>
                        <p>Contact: +977-234-5678</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Discover Nepal. All rights reserved.</p>
    </footer>
</body>
</html>

```
## After choosing Accomodation (say Hotel Everest View) in ./mountain.html we'll get to the accomodation details page
![image](https://github.com/user-attachments/assets/f770cdb9-a259-4035-a98b-a25196bc760d)
![image](https://github.com/user-attachments/assets/29bb77ed-59da-4c17-9794-f15d80e01968)

## Other pages
>Similarly, other pages were designed with consitent styling just with details changed about that particular place

### Pokhara page

![image](https://github.com/user-attachments/assets/253cc05a-a7e6-46dc-99e6-a456e5cff722)
![image](https://github.com/user-attachments/assets/9b04248c-46a2-4301-8f6f-7f7017dff8df)

### Kathmandu Page

![image](https://github.com/user-attachments/assets/536aedd0-4df7-496c-97f6-9c96648123d6)
![image](https://github.com/user-attachments/assets/7b362425-4510-40b5-91c2-6b55e534daf9)

## Styling
The following css has been linked to every webpages for consistent styling
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 1rem;
    text-align: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 1rem;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

.hero {
    position: relative;
    text-align: center;
}

.hero img {
    width: 100%;
    height: auto;
}

.hero-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 1rem;
    border-radius: 8px;
}

.cards {
    padding: 2rem;
    text-align: center;
}

.card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 70px;
    
}

.card {
    border: 1px solid #ddd;
    border-radius: 8px;
    margin: 1rem;
    width: 300px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.card img {
    width: 100%;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

.card-text {
    padding: 1rem;
}

.card-text h3 {
    margin: 0;
}

.card-text a {
    display: block;
    margin-top: 1rem;
    color: #4CAF50;
    text-decoration: none;
}

.card-text a:hover {
    text-decoration: underline;
}

footer {
    background-color: #f1f1f1;
    text-align: center;
    padding: 1rem;
    position: fixed;
    width: 100%;
    bottom: 0;
}

.heroImg {
    max-height: 100vh;
}
```
