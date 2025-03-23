from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed

data = []  # List to hold the data

try:
    # Open the webpage containing the table
    driver.get("https://en.wikipedia.org/wiki/Subdivisions_of_the_Gambia")

    # Wait for the page to load
    time.sleep(3)

    # Find the table with the specified class
    table = driver.find_element(By.CLASS_NAME, 'wikitable')

    # Retrieve all rows from the table body
    rows = table.find_elements(By.TAG_NAME, 'tr')

    # Iterate through each row and extract data
    for index, row in enumerate(rows):
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells:  # Ensure the row has data
            name = cells[0].text
            capital = cells[1].text
            status = cells[2].text
            population = cells[3].text if len(cells) > 3 else "N/A"
            area = cells[4].text if len(cells) > 4 else "N/A"
            density = cells[5].text if len(cells) > 5 else "N/A"

            # Print the extracted data
            print(f"Row {index + 1}:")
            print(f"Name: {name}, Capital: {capital}, Status: {status}, Population: {population}, Area: {area}, Density: {density}")
            print("-" * 40)  # Separator for readability

            # Append the row data to the list
            data.append([name, capital, status, population, area, density])

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()

# Create a DataFrame from the list
df = pd.DataFrame(data, columns=["Name", "Capital", "Status", "Population", "Area", "Density"])

# Save the DataFrame to a CSV file
df.to_csv('gambia_subdivisions.csv', index=False, encoding='utf-8')

# This is asimple selenium Google search automation retrieving information about administrative divisions of The Gambia.
