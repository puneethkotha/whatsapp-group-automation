from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome webdriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code
input("Scan the QR code and press Enter to continue...")

# Function to create a WhatsApp group
def create_whatsapp_group(group_name, participants):
    chat_input = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    chat_input.click()
    chat_input.send_keys('/newgroup\n')
    time.sleep(2)  # Wait for the "New Group" modal to open

    group_name_input = driver.find_element(By.XPATH, '//input[@data-tab="2"]')
    group_name_input.send_keys(group_name)
    group_name_input.send_keys(Keys.ENTER)

    time.sleep(2)  # Wait for the group name to be set
    for participant in participants:
        chat_input.send_keys(participant)
        chat_input.send_keys(Keys.ENTER)
        time.sleep(1)  # Wait for participant to be added

# Call the function to create a WhatsApp group
group_name = "My New Group"
participants = ["John", "Jane", "Mike"]

create_whatsapp_group(group_name, participants)

# Cleanup - close the browser
driver.quit()
