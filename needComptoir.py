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

def need_comptoir_search(val):

    url = "https://neeed.comptoir.co/produits/carte-graphique/rtx-" + val
    # ---------------------------------------------------------------------

    driver = webdriver.Chrome(executable_path=driver_location)
    driver.get(url)

    r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
    r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

    allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
    allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
    allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

    array = []

    for i in range(len(allResult)):
        if allState[i].text == 'EN STOCK!':
            array.append(r_model[i].text)
            array.append(r_price[i].text)
            array.append(allLinkResult[i].get_attribute('href'))

    return array
    # --------génération du fichier excel---------

def excel_generator(array_concat):
    workbook = xlsxwriter.Workbook('needComptoir.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    column = 0
    # arrayindex = array[0:15]
    for data in array_concat:
        if row == 0:
            worksheet.write(row, column, 'NOM')
            column += 1 
            worksheet.write(row, column, 'PRIX')
            column += 1 
            worksheet.write(row, column, 'LIEN')
            column = 0 
            row += 1

        worksheet.write(row, column, data)
        column += 1 
        
        if column == 3:
            column = 0
            row += 1

    workbook.close()
