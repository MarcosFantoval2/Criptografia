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
driver.find_element_by_id('ap_password').send_keys('-CazÁ9')
time.sleep(3)
driver.find_element_by_id('signInSubmit').click()
time.sleep(3)
driver.find_element_by_id('nav-link-accountList-nav-line-1').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@data-card-identifier="SignInAndSecurity"]').click()
time.sleep(3)
driver.find_element_by_id('auth-cnep-edit-password-button').click()
time.sleep(3)
driver.find_element_by_id('ap_password').send_keys('-CazÁ9')
time.sleep(5)
password = driver.find_element_by_id('ap_password_new')
password.send_keys('-CazÁ9m')
time.sleep(5)
password1 = driver.find_element_by_id('ap_password_new_check')
password1.send_keys('-CazÁ9m')
time.sleep(3)
driver.find_element_by_id('cnep_1D_submit_button').click()
time.sleep(15)

driver.quit()