# scrapping
# from datetime import datetime, date, timedelta
import time
# import validators
# import re
# import pandas as pd

# pip install selenium 
# Web Driver module
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.common.exceptions import NoSuchElementException



driver_location = "C:\\Users\\vergu\\Desktop\\chromeDriver\\chromedriver.exe"
binary_location = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location


driver = webdriver.Chrome(executable_path=driver_location)

driver.get('https://www.ldlc.com/recherche/rtx3080/')

# accepter des cookies eyJpZCI6ImYyYjI3MjU0LTMwZWYtNTcxZi1iMjBmLTA1OGM0OWMzOGQ2YiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkxNTIsImV4aXN0aW5nIjp0cnVlfQ

time.sleep(2)
# add cookie for scrappe anyone profile account
driver.add_cookie({"name": "_hjSession_445258", "value": "eyJpZCI6IjFjODRhNDliLTYwYzItNDdjOS1iNGJlLTY4NDNiYWVkYTJlMiIsImNyZWF0ZWQiOjE2NDg1Nzk1OTY0OTUsImluU2FtcGxlIjpmYWxzZX0="})
driver.add_cookie({"name": "_hjSessionUser_445258", "value": "eyJpZCI6ImYyYjI3MjU0LTMwZWYtNTcxZi1iMjBmLTA1OGM0OWMzOGQ2YiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkxNTIsImV4aXN0aW5nIjp0cnVlfQ=="})
# time for cookie
time.sleep(2)

test = []
prix = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[4]/div/div')
nom  = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[1]/div[1]/h3/a')
link = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[1]/div[1]/h3/a') 
stock = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[3]/div/div[2]/div/span')                             

# for s in stock:
#     print (s.text)
# for p in prix:
#     print (p.text)

# for n in nom:
#     print (n.text)

# for l in link:
#     print(l.get_attribute('href'))


# print(len(stock))
# print(len(prix))
# print(len(link))
# print(len(nom))

for i in range(len(stock)):
    if stock[i].text == 'EN STOCK':
        test.append(nom[i].text)
        test.append(prix[i].text)
        test.append(stock[i].text)
        test.append(link[i].get_attribute('href'))

print(len(test))
for tttt in test:
    print(tttt)
    print(':)')


# print(prix)
# item = {
#     'titre': titre,
#     'prix':prix
# }
# json_object = json.dumps(item, indent = 2)
  
# # Writing to sample.json
# with open("sample.json", "w") as outfile:
#     outfile.write(json_object))
# driver.quit()   

