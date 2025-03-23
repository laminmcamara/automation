# selenium automation Google search for multiple queries
# importing important libraries
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Load configuration from JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Set up Chrome options to suppress logging
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')  # Set log level to suppress messages
options.add_argument('headless')  # Uncomment to run in headless mode

# Initialize the Chrome driver
service = Service(config['driver_path'])
driver = webdriver.Chrome(service=service, options=options)

def perform_search(driver, query):
    """
    Perform a search on Google and wait for the results page to load.

    Parameters:
    - driver: The Selenium WebDriver instance.
    - query: The search query string.
    """
    try:
        driver.get(config['url'])  # Navigate to the specified URL
        
        # Wait for the search box to load
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))  # Locator for the search box
        )

        # Enter the search query
        search_box.send_keys(query)
        search_box.submit()  # Submit the search query

        # Wait for the search results page to load
        WebDriverWait(driver, 10).until(
            EC.title_contains(query)  # Check if the title contains the search query
        )
        
        print(f'Test successful: Google search results page loaded for query: {query}.')

    except TimeoutException:
        print('Test failed: Timed out waiting for page to load.')

# Example usage of the perform_search function
if __name__ == "__main__":
    query = config['search_query']  # Get the search query from the config
    perform_search(driver, query)  # Call the search function

    # Close the browser window
    driver.quit()
