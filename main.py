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
binary_location = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location


driver = webdriver.Chrome(executable_path=driver_location)

driver.get('https://www.ldlc.com/fiche/PB00479994.html')
# driver.get('https://www.amazon.com/')
# accepter des cookies eyJpZCI6ImYyYjI3MjU0LTMwZWYtNTcxZi1iMjBmLTA1OGM0OWMzOGQ2YiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkxNTIsImV4aXN0aW5nIjp0cnVlfQ
# results = driver.find_elements_by_class_name("sbloc")
time.sleep(2)
# add cookie for scrappe anyone profile account
driver.add_cookie({"name": "_hjSession_445258", "value": "v6lseQRso1qnoRKkR/ZU8dWpUFyfxCi69uZWKHdKwz9pHPTzvH8ahCbU8t7TgNWfmPBCMK/8DFLev6xzgtEqh69JERPGNR3KWkvsCSD3MujBm9PzvfZB//B50rdJHni4xcxOudRTQ4rFRN6msIlf0ZQ7MDrkc6V2s2B5WjyZOREfmE94PQYO2n9dQozUVHo+"})
driver.add_cookie({"name": "_hjSessionUser_445258", "value": "eyJpZCI6ImYyYjI3MjU0LTMwZWYtNTcxZi1iMjBmLTA1OGM0OWMzOGQ2YiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkxNTIsImV4aXN0aW5nIjp0cnVlfQ=="})
# time for cookie
time.sleep(2)

results = driver.find_element(By.XPATH, '//*[@id="activeOffer"]/div[2]/div[3]/aside/div[1]/div').text
# results = driver.find_elements(By.XPATH, '//*[@id="activeOffer"]/div[2]/div[3]/aside/div[1]/div')

# results = soup.find(id="cookieConsentBanner")
# cookies = driver.get_cookies()
# print(cookies)

print(results)
# driver.quit()   

