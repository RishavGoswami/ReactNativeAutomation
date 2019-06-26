import sys
import os
from selenium import webdriver


path = "/Users/<Your Name>/Desktop/Project/"

# Give the path to your chrome driver
# This driver is for MAC only
browser = webdriver.Chrome('./chromedriver')
browser.get('https://github.com/login')

username = 'Your Username'
password = 'Password'

folderName = str(sys.argv[1])

# Create a new folder with the name
os.mkdir(path+folderName)

# Enter the login
# User ID
python_button = browser.find_element_by_id('login_field')
python_button.clear()
python_button.send_keys(username)
# Password ID
python_button = browser.find_element_by_id('password')
python_button.clear()
python_button.send_keys(password)

# Login button
python_button = browser.find_element_by_name("commit")
python_button.click()

# Navigate to create new project
browser.get('https://github.com/new')

# Repository name for the new project
python_button = browser.find_element_by_id('repository_name')
python_button.send_keys(folderName)

# Privacy // Optional
python_button = browser.find_element_by_id('repository_visibility_private')
python_button.click()

# Submit & quit the browser
python_button.submit()
browser.quit()
