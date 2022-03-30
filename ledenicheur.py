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
driver.add_cookie({"name": "pj:session", "value": "eyJpZCI6IjE5MDI3ZDNiLTJmOTEtNGQ2MS04NTNkLThmZTBmMzI0YThmNSIsInZpZXdlZEV4cGVyaW1lbnRzIjp7fSwiX2V4cGlyZSI6MTk2Mzk5ODQxMTc3NywiX21heEFnZSI6MzE1MzYwMDAwMDAwfQ=="})
driver.add_cookie({"name": "pj:session.sig", "value": "BHuyVyXMbvvc5MD5Knip0_8HTdY"})

time.sleep(2)
allElement = driver.find_elements(By.XPATH,'//*[@id="#products"]/ul[1]/li')

test = []
list_names = driver.find_elements(By.XPATH, ' //*[@id="#products"]/ul[1]/li/a/div[2]/span')
list_prices = driver.find_elements(By.XPATH, '//*[@id="#products"]/ul[1]/li/a/div[3]/div/div/div/div/span[2]')
list_links = driver.find_elements(By.XPATH, '//*[@id="#products"]/ul[1]/li/a')
all_results = driver.find_elements(By.XPATH, '//*[@id="#products"]/ul[1]/li')                                
                                                
# for p in list_prices:
#      print(p.text)
#      print(':)')
     
# for n in list_names:
#     print(n.text)
#     print(':)')

# for l in list_links:
#     print(l.get_attribute('href'))
#     print(':)')
print('list_names')
print(len(list_names))
print('list_prices')
print(len(list_prices))
print('list_links')
print(len(list_links))
print('all_results')
print(len(all_results))


# for n in range(len(all_results)):
#     test.append(list_links[n].get_attribute('href'))
#     test.append(list_names[n].text)
#     test.append(list_prices[n].text)

