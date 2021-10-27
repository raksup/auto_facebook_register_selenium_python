'''
Author: Raksup
Date:  October 27, 2021
'''

import time
import details

from selenium import webdriver
#webdriver import for Mozilla Firefox.
from selenium.webdriver.firefox import service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#path for webdriver executable file
s = service.Service("./geckodriver.exe")
driver = webdriver.Firefox(service=s)

driver.maximize_window()
driver.get('https://www.facebook.com/')

#selects the Create New Account button
driver.find_element(By.XPATH, "//*[text()='Create New Account']").click()
time.sleep(3)

#The signup form pops up and now we need to add the details in the form to complete the signup.
driver.find_element(By.NAME, "firstname").send_keys(details.NAME)
driver.find_element(By.NAME, "lastname").send_keys(details.SURNAME)
driver.find_element(By.NAME, "reg_email__").send_keys(details.REGISTRATION_EMAIL)
time.sleep(1)
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(details.REGISTRATION_EMAIL)
driver.find_element(By.ID, "password_step_input").send_keys(details.PASSWORD)
month= Select(driver.find_element(By.XPATH, "//select[@title='Month']"))
month.select_by_visible_text(details.BIRTH_MONTH)
day= Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text(details.BIRTH_DAY)
year= Select(driver.find_element(By.XPATH, "//select[@title='Year']"))
year.select_by_visible_text(details.BIRTH_YEAR)

driver.find_element(By.XPATH, "//label[text()='{}']".format(details.GENDER)).click()

#Submit the details for signup
driver.find_element(By.NAME, "websubmit").click()

#closes the session
driver.quit()