from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome driver
driver = webdriver.Chrome()


# Open Google login page
driver.get("https://accounts.google.com")


# Find and fill in the email field
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("your@email.com")
email_field.send_keys(Keys.RETURN)

# Wait for the password field to appear
password_field = WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

# Fill in the password field
password_field.send_keys("your_password")
password_field.send_keys(Keys.RETURN)

# Wait for the Google homepage to load
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "gb")))

# Open Google Pictures
# driver.get("https://photos.google.com")

# Load and delete each URL

import json

# Load the URLs from the JSON file
with open("./url_remove.json", "r") as file:
    urls = json.load(file)

print(urls)

for url in urls:
    # Open the URL in Google Pictures
    driver.get(url)

    # Wait for the delete button to appear
    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Delete']"))
    )

    # Click the delete button
    delete_button.click()

    # Confirm the deletion
    confirm_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Delete']"))
    )
    confirm_button.click()

# Close the browser
driver.quit()
