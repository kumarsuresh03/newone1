from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
# Initialize the WebDriver (assuming you have Chrome WebDriver installed)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://duckduckgo.com/")
time.sleep(8)

# Find the search box element by its ID, name, XPath, or CSS selector
search_box = driver.find_element(By.ID, "searchbox_input")  # Replace "searchBoxId" with the actual ID of the search box

search_query = "Allu Arjun"
search_box.send_keys(search_query)


search_box.send_keys(Keys.RETURN)


time.sleep(5)
# Find the link element using its ID, class name, XPath, etc.
link_element = driver.find_element(By.CSS_SELECTOR, "a[data-testid='result-title-a']")

# Click the link element
link_element.click()
time.sleep(4)
# Close the WebDriver
driver.quit()
