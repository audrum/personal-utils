from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# List of URLs to randomly choose from
urls = [
    'https://www.google.com',
    'https://www.yahoo.com',
    'https://www.bing.com',
    'https://www.reddit.com',
    'https://www.wikipedia.org'
]

# Create a new browser window
browser = webdriver.Firefox()

# Navigate to a random URL
random_url = random.choice(urls)
browser.get(random_url)

# Wait for the page to load and the cookie banner to appear
wait = WebDriverWait(browser, 10)
cookie_banner = wait.until(EC.presence_of_element_located((By.ID, 'cookie-banner')))

# Accept the cookies
accept_button = cookie_banner.find_element(By.XPATH, '//button[text()="Accept"]')
accept_button.click()

# Wait for the page to finish loading
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Close the browser window
browser.quit()
