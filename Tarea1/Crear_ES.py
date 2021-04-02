from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.amazon.es')
time.sleep(5)
driver.find_element_by_id('sp-cc-accept').click()
time.sleep(5)
driver.find_element_by_id('nav-link-accountList-nav-line-1').click()
time.sleep(5)
driver.find_element_by_id('auth-create-account-link').click()
time.sleep(5)
driver.find_element_by_id('ap_customer_name').send_keys(random.choice(Nombre))
driver.find_element_by_id('ap_email').send_keys('criptotareas@gmail.com')
driver.find_element_by_id('ap_password').send_keys('-CazÁ9')
driver.find_element_by_id('ap_password_check').send_keys('-CazÁ9')
time.sleep(5)
driver.find_element_by_id('ap_password_check').send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()
