## Getting Started With Python Selenium

```cpp
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()  # Assumes ChromeDriver is in PATH

# Navigate to python.org
driver.get("https://python.org")

# Print the title of the page
print("Page title is:", driver.title)

# Close the browser
driver.quit()

```
>Note: Install chromedriver and keep it in path

## 
