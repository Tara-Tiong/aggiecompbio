from selenium import webdriver
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Open the page
driver.get('https://aggie-website-portfolio.my.canva.site/computational')
time.sleep(5)  # Wait for the page to load fully

# Get the page's HTML source
html_content = driver.page_source

# Save it to a file
with open('canva.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

# Close the driver
driver.quit()

print("Page saved exactly as 'exact_copy.html'")
