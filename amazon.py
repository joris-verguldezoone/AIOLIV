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


url = 'https://www.amazon.fr'

driver.get(url)

driver.add_cookie({"name": "session-token", "value": "rnZ7aQxevcvrs7Bc73sFhRHtUweZmzT1/o3jB/AG/16McI+rqS+hspm+NSAvF2lQ4ghLaLEgbFe0XJ9FBYEMhpoj0lZdwEwC5TI9ur/lFrZ+XDSC6wzoiadVwRHd9Te6AkOV3hECO2iWZIdgrZf4K4ZS1CiZnmUTm41ED+kWWVjNJw9Ma8mnYWHW3ISqQuTq"})

time.sleep(2)

search_bar = driver.find_element(By .ID,'twotabsearchtextbox')

motClef = input(" enter a string : ")
time.sleep(1)
search_bar.send_keys(motClef)
search_bar.send_keys(Keys.RETURN)



# search_btn = driver.find_element(By .ID, 'nav-search-submit-button') 
# print (search_btn.text)
# search_btn.click()
# driver.get('https://www.amazon.com/')
# accepter des cookies eyJpZCI6ImYyYjI3MjU0LTMwZWYtNTcxZi1iMjBmLTA1OGM0OWMzOGQ2YiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkxNTIsImV4aXN0aW5nIjp0cnVlfQ
# results = driver.find_elements_by_class_name("sbloc")
# add cookie for scrappe anyone profile account
# time for cookie



# results = driver.find_elements(By.XPATH, '//*[@id="activeOffer"]/div[2]/div[3]/aside/div[1]/div')

# results = soup.find(id="cookieConsentBanner")
# cookies = driver.get_cookies()
# print(cookies)
# driver.quit()   

# titre = driver.find_element(By.ID, 'productTitle');




driver.get('https://www.amazon.fr/s?k=rtx+3080&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss')


div = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/h2/a').get_attribute('href')

driver.get(div)

time.sleep(2)

asin = driver.find_element(By.XPATH, '//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td').text



print(asin)


# /html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div/div[2]/div[1]/h2/a