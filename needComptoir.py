import time
import json
import xlsxwriter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command

driver_location = "chromedriver.exe"
binary_location = binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location)

driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3080/')
# driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3060/')


time.sleep(2)
# add cookie for scrappe anyone profile account
# driver.add_cookie({"name": "_hjSession_445258", "value": "eyJpZCI6ImU1ZmJmNjQ0LTUzOTctNDBmZi04N2VlLWFiMmJkZGIwMWNjYiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkyNjUsImluU2FtcGxlIjpmYWxzZX0="})
# driver.add_cookie({"name": "_hjSessionUser_445258", "value": "eyJpZCI6ImYyYjI3MjU0LTMwZWYtNTcxZi1iMjBmLTA1OGM0OWMzOGQ2YiIsImNyZWF0ZWQiOjE2NDg1MDU4NDkxNTIsImV4aXN0aW5nIjp0cnVlfQ=="})
# time for cookie
test = []
r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

for i in range(len(allResult)):
    # allLinkResult[i]
    # allState[i]
    # r_model[i]
    # r_price[i]
    if allState[i].text == 'EN STOCK!':
        test.append(r_model[i].text)
        test.append(r_price[i].text)
        test.append(allLinkResult[i].get_attribute('href'))

# for ll in test: 
#     print(ll)

workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

for data in (test):
    worksheet.write(row, column, data)
    row +=1
       
workbook.close()

   



