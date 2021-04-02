from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome('./chromedriver')
driver.get('https://simple.ripley.cl')
time.sleep(3)
driver.find_element_by_class_name('my-account').click()
time.sleep(2)
driver.find_element_by_name('ws_username').send_keys("19477733-7")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="ripley-sticky-header"]/section/nav/ul/li[2]/div/div/div/div/div/div/div/div/div[1]/form/div/div[2]/div/input').send_keys('-CazÁ9')
time.sleep(1)
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(15)
driver.quit()
