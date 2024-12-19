import sys
print(sys.path)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse

# Create an ArgumentParser to handle command-line arguments
parser = argparse.ArgumentParser(description="Loop through a URL using Selenium.")
parser.add_argument("url", nargs="?", default="https://{change_into_your_domain}/pageshieldforcecsp", help="URL to visit (default: https://{change_into_your_domain}/pageshieldforcecsp)")
parser.add_argument("num_loops", nargs="?", type=int, default=100, help="Number of times to loop through the URL with pageshieldforcecsp to force CSP (default: 100)")
args = parser.parse_args()
args = parser.parse_args()


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Loop through the URL
for i in range(args.num_loops):
    try:
        # Open the URL in the browser
        driver.get(args.url)

        # Perform actions on the web page (customize this part)

        # Print the page title
        print(f"Loop {i + 1} - Page Title: {driver.title}")

        # Wait for a few seconds before moving to the next loop
        time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Close the browser
driver.quit()
