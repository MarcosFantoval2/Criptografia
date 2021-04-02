from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


RUT = ("122805298","126727240","143074110","86946777","215127761","122874281","145552613","120001809","84289426")
Nombre = ("PEDRO", "JUAN","DIEGO","JOSE","MARIA","MARCOS","JESUS","MIGUEL","GABRIEL","ANTONIO","MATIAS","CARLOS","ANGEL","JOSE LUIS","ALEJANDRO","MANUELA","DANIELA", "DANIEL","ROBERTO","FERNANDO","FRANCISCO")
Apellido = ("GONSALEZ", "SILVA", "DIAS", "MARTINES", "FAUNDES","ROJAS", "PEREZ", "CONTRERAS", "MEDEL", "BRAVO","ISLA", "FERNANDES", "SANCHEZ", "MESSI", "VARGAS", "ORELLANA")


driver = webdriver.Chrome('./chromedriver')
driver.get('https://simple.ripley.cl')
time.sleep(5)
driver.find_element_by_class_name('my-account').click()
time.sleep(5)
driver.find_element_by_class_name('signup__link').click()
time.sleep(1)
driver.find_element_by_name('ws_username').send_keys(random.choice(RUT))
time.sleep(1)
driver.find_element_by_name('firstName').send_keys(random.choice(Nombre))
time.sleep(1)
driver.find_element_by_name('lastName').send_keys(random.choice(Apellido))
time.sleep(1)
driver.find_element_by_name('email').send_keys('criptotareas@gmail.com')
time.sleep(1)
driver.find_element_by_name('password').send_keys('-CazÁ9')
time.sleep(1)
driver.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(10)
driver.quit()

