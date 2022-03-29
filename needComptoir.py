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

# ---------------------------------------------------------------------

driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3060/')

r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

array3060 = []

for i in range(len(allResult)):
    if allState[i].text == 'EN STOCK!':
        array3060.append(r_model[i].text)
        array3060.append(r_price[i].text)
        array3060.append(allLinkResult[i].get_attribute('href'))

# ---------------------------------------------------------------------

driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3060-ti/')

r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

array3060ti = []

for i in range(len(allResult)):
    if allState[i].text == 'EN STOCK!':
        array3060ti.append(r_model[i].text)
        array3060ti.append(r_price[i].text)
        array3060ti.append(allLinkResult[i].get_attribute('href'))

# ---------------------------------------------------------------------

driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3070/')

r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

array3070 = []

for i in range(len(allResult)):
    if allState[i].text == 'EN STOCK!':
        array3070.append(r_model[i].text)
        array3070.append(r_price[i].text)
        array3070.append(allLinkResult[i].get_attribute('href'))

# ---------------------------------------------------------------------

driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3080/')

r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

array3080 = []

for i in range(len(allResult)):
    if allState[i].text == 'EN STOCK!':
        array3080.append(r_model[i].text)
        array3080.append(r_price[i].text)
        array3080.append(allLinkResult[i].get_attribute('href'))

# ---------------------------------------------------------------------

driver.get('https://neeed.comptoir.co/produits/carte-graphique/rtx-3090/')

r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')

array3090 = []

for i in range(len(allResult)):
    if allState[i].text == 'EN STOCK!':
        array3090.append(r_model[i].text)
        array3090.append(r_price[i].text)
        array3090.append(allLinkResult[i].get_attribute('href'))

# ---------------------------------------------------------------------

# for ll in test: 
#     print(ll)

# --------génération du fichier excel---------

workbook = xlsxwriter.Workbook('needComptoir.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0
arrayindex = array3060[0:15]

for data in arrayindex:
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

   



