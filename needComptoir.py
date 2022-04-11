from asyncio import sleep
import json
import xlsxwriter

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command

#warning ignore 







driver_location = "chromedriver.exe"
binary_location = binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location

# def waitFunction(element_id):
#         element_id=(NoSuchElementException,StaleElementReferenceException,)
#         new_element = WebDriverWait(driver_location, 10,ignored_exceptions=IGNORE_EXCEPTION_DETAIL)\
#         .until(expected_conditions.presence_of_element_located((By.XPATH, element_id)))
#         return new_element

def need_comptoir_search(val):

    url = "https://neeed.comptoir.co/produits/carte-graphique/rtx-" + val
    # ---------------------------------------------------------------------

    driver = webdriver.Chrome(executable_path=driver_location)
    driver.get(url)
    # sleep(2)
    # add cookie for scrappe anyone profile account
    driver.add_cookie({"name": "ci_session", "value": "r24tnk996hur4crqsul2vbpst8etceli"})
    # for cookie
    # sleep(2)
    print("NeedComptoir_1")

    r_price = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[3]/span[1]')
    r_model = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[2]/div[1]/a/h2') 

    allResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div')
                                                # /html/body/div[2]/div[1]/div[6]/div[4]
    allLinkResult = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a')
    allState = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div[6]/div[4]/div/div/div[4]/a/button')
    # sleep(5)

    # r_price = waitFunction(r_price)
    # r_model = waitFunction(r_model)
    # allResult = waitFunction(allResult)
    # allLinkResult = waitFunction(allLinkResult)
    # allState = waitFunction(allState)

    array = []
    print(len(allResult))
    print(type(allResult))
    print("NeedComptoir_2")
    # sleep(5)

    for i in range(len(allResult)):
        if allState[i].text != '':
            if allState[i].text == 'EN STOCK!':
                # print(i)
                # print(r_model[i].text)
                # print(allLinkResult[i].get_attribute('href'))
                # print(r_price[i].text)
                try:
                    r_model[i].text, r_price[i].text ,allLinkResult[i].get_attribute('href')
                except NameError:
                    print('undefined value of result from dom')
                else:
                    # print("sure, it was defined.")
                    array.append(r_model[i].text)
                    array.append(r_price[i].text) # mettre des securite isset 
                    array.append(allLinkResult[i].get_attribute('href'))

    print("NeedComptoir_3")
    sleep(5)
    
    return array
    # --------génération du fichier excel---------

def excel_generator(array_concat, bestPriceTab):
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

    row += 5 
    column = 0
    print('bestPriceLen')
    print(len(bestPriceTab))
    print('bestPriceLen')
    worksheet.write(row, column, 'NOM')
    column += 1 
    worksheet.write(row, column, 'PRIX')
    column = 0 
    
    for key, data in bestPriceTab.items():
        worksheet.write(row, column, key)
        column += 1
        worksheet.write(row, column, data)
        row += 1
            
        if column == 1:
            column = 0
       

    workbook.close()
