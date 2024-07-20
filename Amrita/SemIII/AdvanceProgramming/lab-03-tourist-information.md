# UID Lab - 3 Tourist Information Webpage

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
                <!-- Add more cards as needed -->
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
                <!-- Add more cards as needed -->
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
