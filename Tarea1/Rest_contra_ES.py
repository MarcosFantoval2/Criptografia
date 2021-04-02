from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.amazon.es')
time.sleep(3)
driver.find_element_by_id('sp-cc-accept').click()
time.sleep(5)
driver.find_element_by_id('nav-link-accountList-nav-line-1').click()
time.sleep(5)
driver.find_element_by_id('ap_email').send_keys('criptotareas@gmail.com')
time.sleep(3)
driver.find_element_by_id('continue').click()
time.sleep(3)
driver.find_element_by_id('auth-fpp-link-bottom').click()
time.sleep(3)
driver.find_element_by_id('continue').click()
time.sleep(90)#variar el tiempo segun pc e internet
driver.find_element_by_class_name('a-autoid-0').click()
time.sleep(3)
driver.find_element_by_id('ap_fpp_password').send_keys('-CazÁ9m')
time.sleep(3)
driver.find_element_by_id('ap_fpp_password_check').send_keys('-CazÁ9m')
time.sleep(60)

driver.quit()