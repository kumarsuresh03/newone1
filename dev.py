from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("file:///C:/Users/MyPc/Desktop/CA!/lab%20automatiom.html")

time.sleep(2)

# Interact with text input
name_input = driver.find_element(By.ID, "text")
name_input.send_keys("Surya")

time.sleep(2)

textarea = driver.find_element(By.ID, "textarea")

# Input text into the textarea
textarea.send_keys("I Don't have any house adress")

time.sleep(2)


checkbox = driver.find_element(By.ID, "checkbox1")
checkbox.click()

time.sleep(2)



greet_button = driver.find_element(By.ID, "rad1")
greet_button.click()

time.sleep(2)


dropdown_element = driver.find_element(By.ID,"country")
dropdown = Select(dropdown_element)
dropdown.select_by_value("india")

time.sleep(2)

submit_button = driver.find_element(By.ID, "button")
submit_button.click()

time.sleep(2)

driver.quit()