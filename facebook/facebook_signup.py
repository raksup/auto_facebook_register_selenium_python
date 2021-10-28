'''
Author: Raksup
Date:  October 27, 2021
'''

import time
import facebook_details

from selenium import webdriver
#webdriver import for Mozilla Firefox.
from selenium.webdriver.firefox import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#path for webdriver executable file
s = service.Service(facebook_details.WEB_DRIVER_PATH)
driver = webdriver.Firefox(service=s)

driver.maximize_window()
driver.get('https://www.facebook.com/')

#selects the Create New Account button
driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
time.sleep(2)

#The signup form pops up and now we need to add the details in the form to complete the signup.
driver.find_element(By.NAME, "firstname").send_keys(facebook_details.NAME)
driver.find_element(By.NAME, "lastname").send_keys(facebook_details.SURNAME)
driver.find_element(By.NAME, "reg_email__").send_keys(facebook_details.REGISTRATION_EMAIL)
time.sleep(1)
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(facebook_details.REGISTRATION_EMAIL)
driver.find_element(By.ID, "password_step_input").send_keys(facebook_details.PASSWORD)
month= Select(driver.find_element(By.XPATH, "//select[@title='Month']"))
month.select_by_visible_text(facebook_details.BIRTH_MONTH)
day= Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text(facebook_details.BIRTH_DAY)
year= Select(driver.find_element(By.XPATH, "//select[@title='Year']"))
year.select_by_visible_text(facebook_details.BIRTH_YEAR)

driver.find_element(By.XPATH, "//label[text()='{}']".format(facebook_details.GENDER)).click()

#Submit the details for signup
driver.find_element(By.NAME, "websubmit").click()

#closes the session
driver.quit()