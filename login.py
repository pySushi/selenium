# import dependencies
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define inputs for login
site_url = "" # login url
login_username="" # login username
login_password = "" # login password

login_selector = "" # css selector for the login container
username_selector = "" # css selector for the username field
password_selector = "" # css selector for the password field
submit_selector = "" # css selector for the login button

# define web driver and the wait condition
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# open login page using driver
driver.set_window_size(1024, 768) # optional, setting up of the window size
driver.get(site_url)

# wait untill login container is available
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_selector)))

# wait untill login container is available, locate it and input username
username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, username_selector)))
username.send_keys(login_username)

# wait untill password field is available, locate it and input password
password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, password_selector)))
password.send_keys(login_password)

# wait untill submit button is available, locate it and click
submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, submit_selector)))
submit.click()

/* congratulations on successfully logging in */
