# how to test facebook login automation using selenium
# Import necessary libraries from Selenium and OS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Get Facebook credentials from environment variables
email = os.getenv("FB_EMAIL")  # User's email for Facebook login
password = os.getenv("FB_PASSWORD")  # User's password for Facebook login

# Initialize the Chrome browser
browser = webdriver.Chrome()

# Navigate to the Facebook login page
browser.get("http://www.facebook.com/login")

try:
    # Wait for the email input field to be present
    username = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    print("Username field found.")

    # Wait for the password input field to be present
    password_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "pass"))
    )
    print("Password field found.")

    # Wait for the login submit button to be present
    submit = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "login"))
    )
    print("Submit button found.")

    # Check if all required fields are found and perform login
    if username and password_field and submit:
        username.send_keys(email)  # Enter the email into the username field
        password_field.send_keys(password)  # Enter the password into the password field
        submit.click()  # Click the submit button to log in
    else:
        print("One or more elements are None.")

except Exception as e:
    # Handle any exceptions that occur during the process
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    browser.quit()  # Close the browser
