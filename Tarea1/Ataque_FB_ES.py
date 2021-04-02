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
for i in range(30):
    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys("10"+str(i)+"94"+str(i+10)+"6")
    password.send_keys(Keys.ENTER)
    #time.sleep(1)
    time.sleep(10)
time.sleep(20)
driver.quit()