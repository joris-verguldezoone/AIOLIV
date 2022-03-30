# scrapping
# from datetime import datetime, date, timedelta
import time
# import validators
# import re
# import pandas as pd

# pip install selenium 
# Web Driver module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.common.exceptions import NoSuchElementException



driver_location = "C:\\wamp64\\www\\AIOLIV\\chromedriver.exe"
binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location


driver = webdriver.Chrome(executable_path=driver_location)

driver.get('https://ledenicheur.fr/search?search=rtx3080')
time.sleep(2)
driver.add_cookie({"name": "pj:session", "value": "eyJpZCI6IjE3ZDIwYzc5LWIxZDQtNGRjYS1hM2JmLTZlNDA0ZTc4ZTVmMiIsInZpZXdlZEV4cGVyaW1lbnRzIjp7fSwiY29va2llX2NvbnNlbnRfdmVyc2lvbiI6IjQiLCJfZXhwaXJlIjoxOTYzOTE4MTgyNjM1LCJfbWF4QWdlIjozMTUzNjAwMDAwMDB9"})
driver.add_cookie({"name": "pj:session.sig", "value": "xlV8YcNKiHc0p1FNr74t2A22JPU"})

time.sleep(2)

list_names = driver.find_element(By.XPATH, '//*[@id="#products"]/ul/li[2]/a/div[2]/span').text
list_prices = driver.find_element(By.XPATH, '//*[@id="#products"]/ul/li[2]/a/div[3]/div/div/div/div/span[2]').text
list_links = driver.find_element(By.XPATH, '//*[@id="#products"]/ul/li[1]/a').get_attribute('href')

# Le list des links de fonctionne pas - impossible de récupérer le lien



print(list_links)



