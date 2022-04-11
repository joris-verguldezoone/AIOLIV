# scrapping

# from datetime import datetime, date, timedelta
from asyncio import sleep
import time
# import validators
# import re
# import pandas as pd
# pip install selenium 
# Web Driver module
import json
from traceback import print_tb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.common.exceptions import NoSuchElementException
import testamazon
import needComptoir
import GPUTracker

driver_location = "chromedriver.exe"
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

ldlcResult = []
prix = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[4]/div/div')
nom  = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[1]/div[1]/h3/a')
link = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[1]/div[1]/h3/a') 
stock = driver.find_elements(By.XPATH, '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/div[2]/ul/li/div[2]/div[3]/div/div[2]/div/span')                             


for i in range(len(stock)):
    # print(stock[i].text)
    # print(len(stock[i].text))
    if stock[i].text != 'RUPTURE' and (len(stock[i].text) < 9):
        ldlcResult.append(nom[i].text)
        ldlcResult.append(prix[i].text)
        # ldlcResult.append(stock[i].text)
        ldlcResult.append(link[i].get_attribute('href'))

print(len(stock))
i = 1
j = 0
arr = []
for product in ldlcResult: # fonctionne pour un tableau de 3 element par case dont le deuxieme est le prix 
    i = i + 1
    if i == 3:
        i = 0
        string = product.replace(' ', '')
        price = string.replace('€', '.')  
        print(float(price))
        arr.append(float(price))

def conversionDollarToEuro(args):
    arr = []
    coefConversion = 1.09
    for value in args:
        print('conversion')
        print(value)
        print(value*coefConversion)
        print('conversion')
        arr.append(value*coefConversion)
    return arr


def bestPrice(arr): 
    temp = 0
    for price in arr:
        if temp == 0:
            temp = price
        if price < temp:
            temp = price
    # print(temp) # c'est le meilleur prix de ldlc
    return temp


def app():
    val = input("Entrez le modèle de RTX: ")
    gpuTrackerResult = "unUsed"
    bestPriceGpuTracker = "unUsed" 
    arrayConcat = [] 
    if val == '3080':
        gpuTrackerResult = GPUTracker.gpu_tracker_search()
        bestPriceGPUTracker = bestPrice(gpuTrackerResult)

    # try:
    #     gpuTrackerResult, bestPriceGPUTracker
    # except NameError:
    #     print('undefined GPUTracker result and best price')
    # else:
    #     print("sure, it was defined.")
    
    needComptoirResult = needComptoir.need_comptoir_search(val)
    # sleep(15)
    i = 1
    converted_nc_product = []
    # sleep(5)
    for nC_product in needComptoirResult: # fonctionne pour un tableau de 3 element par case dont le deuxieme est le prix 
        i = i + 1
        if i == 3:
            i = 0
            string = nC_product.replace(',', '.')
            var = string.replace(' ', '')
            price = var.replace('€', '') 
            print(price) 
            # print(float(price))
            converted_nc_product.append(price)
    
    # sleep(5)
    bestPrice_nc_product = bestPrice(converted_nc_product)
    
    amazonResult = testamazon.main(val)
    i = 1
    j = 0
    arrayAmazon = []
    for product in amazonResult: # fonctionne pour un tableau de 3 element par case dont le deuxieme est le prix 
        i = i + 1
        if i == 3:
            i = 0
            print(product)
            if not (product is None):
                noDollar = product.replace('$', '')  
                price = noDollar.replace(',', '')  
                arrayAmazon.append(float(price))
                print(price)

    # sleep(2)

    arrayAmazonEuro = conversionDollarToEuro(arrayAmazon)
    bestAmazonPrice = bestPrice(arrayAmazonEuro)
    bestPriceLdlc = bestPrice(arr)

    print('Amazon Price')
    print(bestAmazonPrice)
    print('Amazon Price')
    print('bestPrice_nc_product')
    print(bestPrice_nc_product)
    print('bestPrice_nc_product')
    print('bestPriceGPUTracker')
    print(bestPriceGPUTracker)
    print('bestPriceGPUTracker')
    print("bestPriceLdlc")
    print(bestPriceLdlc)
    print("bestPriceLdlc")
    # sleep(2)
    bestPriceTab = {'neeedComptoir': bestPrice_nc_product, 'gpuTracker' : bestPriceGPUTracker, 'ldlc' : bestPriceLdlc, "amazon": bestAmazonPrice,}
    arrayConcat =  needComptoirResult + gpuTrackerResult + ldlcResult + amazonResult

    # sleep(2)

    needComptoir.excel_generator(arrayConcat,bestPriceTab)

# sleep(10)
# print(gpuTrackerResult)
# test.append(gpuTrackerResult)

# print('qzseslfkhjkqzlkefjlkjqledkjlkjeldkjlkjzezf')
# for t in test: 
#     print(t)
# print('qzseslfkhjkqzlkefjlkjqledkjlkjeldkjlkjzezf')

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

app()