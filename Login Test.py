# using selenium to test a web login
# importing necessary libraries
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome driver (you can choose another browser if needed)
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://coursera.org/login")  # Navigate to the login page

    def test_login(self):
        # Locate the email and password fields
        print("Attempting to find email field...")
        email_field = self.driver.find_element(By.NAME, "email")
        print("Attempting to find password field...")
        password_field = self.driver.find_element(By.NAME, "password")

        # Input test email and password
        email_field.send_keys("lam@gmail.com")  # Replace with a valid test email
        password_field.send_keys("mypassword")  # Replace with a valid test password

        # Submit the form by sending the RETURN key
        password_field.send_keys(Keys.RETURN)  # Only need to submit once

        # Wait for the page to load and check for an element that indicates successful login
        try:
            # Adjust the locator based on the expected element after login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cds-1 css-7dqzpp cds-3 cds-grid-item cds-48"))  # Example class name after login
            )
            print("Login successful!")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.fail("Login test failed.")

        # Optionally check if the URL has changed or contains a specific string
        self.assertNotIn("login", self.driver.current_url)  # Ensure we are not on the login page

    @classmethod
    def tearDownClass(cls):
        # Close the browser after tests are done
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
