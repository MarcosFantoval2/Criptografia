from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui


driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome('./chromedriverd')
driver.get('https://simple.ripley.cl')
time.sleep(3)
driver.find_element_by_class_name('my-account').click()
time.sleep(3)
driver.find_element_by_class_name('credentials__link').click()
time.sleep(3)
driver.find_element_by_name('wc_username').send_keys('19477733-7')
time.sleep(3)
pyautogui.press('enter')
time.sleep(90)#variar el tiempo segun pc e internet
pyautogui.press('enter')
time.sleep(3)
driver.find_element_by_id('password').send_keys('-CazÁ9m')
time.sleep(3)
driver.find_element_by_id('password2').send_keys('-CazÁ9m')
time.sleep(60)

driver.quit()