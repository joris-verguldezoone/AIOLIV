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



driver_location = "chromedriver.exe"
binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location


driver = webdriver.Chrome(executable_path=driver_location)

driver.get('https://ledenicheur.fr/search?search=rtx3080')
time.sleep(2)
driver.add_cookie({"name": "pj:session", "value": "eyJpZCI6IjE3ZDIwYzc5LWIxZDQtNGRjYS1hM2JmLTZlNDA0ZTc4ZTVmMiIsInZpZXdlZEV4cGVyaW1lbnRzIjp7fSwiY29va2llX2NvbnNlbnRfdmVyc2lvbiI6IjQiLCJfZXhwaXJlIjoxOTYzOTE4MTgyNjM1LCJfbWF4QWdlIjozMTUzNjAwMDAwMDB9"})
driver.add_cookie({"name": "pj:session.sig", "value": "xlV8YcNKiHc0p1FNr74t2A22JPU"})

time.sleep(2)
allElement = driver.find_elements(By.XPATH,'//*[@id="#products"]/ul[1]/li')

test = []
list_names = driver.find_elements(By.XPATH, ' //*[@id="#products"]/ul[1]/li/a/div[2]/span')
list_prices = driver.find_elements(By.XPATH, '//*[@id="#products"]/ul[1]/li/a/div[3]/div/div/div/div/span[2]')
list_links = driver.find_elements(By.XPATH, '//*[@id="#products"]/ul[1]/li/a')
                                        



# print(len(allElement))
# print('monvierMtn + allelement')
# print(allElement[47].text)
# print(allElement[50].text)
# print('coucou')
# print('monvierMtn + list_link')
# print(list_links[47].text)
# print(list_links[51].text)
# print('coucou')


print(len(list_names))
print(len(list_prices))
print(len(list_links))
print(list_names[47].text)
print(list_links[47].get_attribute('href'))
print(list_prices[47].text)

# for i in range(len(list_links)):
#     test.append(list_prices[i].text)
#     test.append(list_links[i].get_attribute('href'))
#     test.append(list_names[i].text)
    
# for e in test:
#     print(e)

    # if allState[i].text == 'EN STOCK!':
# print(list_links)