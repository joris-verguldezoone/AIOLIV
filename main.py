# il manque la partie "voir plus" pour la selection des produits (seulement les premiers produit de la page)





# scrapping



import time
import json


# pip install selenium 
# Web Driver module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command



driver_location = "C:\\Users\\Frede\\OneDrive\\Bureau\\les repositorys\\AIOLIV\\chromedriver.exe"
binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location


driver = webdriver.Chrome(executable_path=driver_location)

driver.get('https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?textualSearch=rtx3080')
# time pour get
time.sleep(2)

driver.add_cookie({"name": "SESSION", "value": "NmNiODBmZGUtOTZkOC00YmFhLWJkYjItNTFiZjRiODgxNjAw"})
# time pour cookie
time.sleep(2)

recup = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div[2]/main/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/a/div')
 
test=[]
price = driver.find_elements(By.XPATH,'//*[@id="facet-search-results"]/div[2]/div/div/div/div/div/a/div/div[3]/div/div/div[1]/span')
nom = driver.find_elements(By.XPATH,  '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div/a/div/div[2]/h3')
stok = driver.find_elements(By.XPATH, '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div/div/div[2]')

link = driver.find_elements(By.XPATH, '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div[2]/div/div/div[1]/a')
                                       

allresults = driver.find_elements(By.XPATH, '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div[2]/div/div/div[1]/a')

# for l in link:
#     print(l.get_attribute('href'))

# for p in price:
#      print(p.text)
#      print(':)')

# for n in nom:
#     print(n.text)
#     print(':)')
# for s in stok:
#     print(s.text)
#     print(':)')

# print(len(allresults))
# print(len(price))
# print(len(nom))
# print(len(stok))
for i in range(len(allresults)):
    if stok[i].text == 'En stock':
        test.append(nom[i].text)
        test.append(price[i].text)
        test.append(stok[i].text)
        test.append(link[i].get_attribute('href'))


print(test)

for zsdfg in test:
    print(zsdfg) 
