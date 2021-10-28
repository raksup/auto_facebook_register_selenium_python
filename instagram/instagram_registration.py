'''
Author: Raksup
Date:  October 28, 2021
'''


import time
import instagram_details

from selenium import webdriver
from selenium.webdriver.firefox import service
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


s = service.Service(instagram_details.WEB_DRIVER_PATH)
driver = webdriver.Firefox(service=s)

driver.maximize_window()
driver.get('https://www.instagram.com/')
#Clicks the sign up link in the bottom
wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign up']"))).click()

#Entering the user input
wait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='emailOrPhone']"))).send_keys(instagram_details.MOBILE_OR_EMAIL)
driver.find_element(By.NAME, 'fullName').send_keys(instagram_details.FULLNAME)
driver.find_element(By.NAME, 'username').send_keys(instagram_details.USERNAME)
driver.find_element(By.NAME, 'password').send_keys(instagram_details.PASSWORD)

#Submit the details for signup
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)
#closes the session
driver.quit()