from selenium import webdriver
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Open the page
driver.get('http://127.0.0.1:5500/home/home/index.html')
time.sleep(5)  # Wait for the page to load fully

# Get the page's HTML source
html_content = driver.page_source

# Save it to a file
with open('exact_copy.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# Close the driver
driver.quit()

print("Page saved exactly as 'exact_copy.html'")
