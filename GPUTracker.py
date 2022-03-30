# scrapping
# il manque la partie "voir plus" pour la selection des produits (seulement les premiers produit de la page)

import time

# pip install selenium 
# Web Driver module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver import  DesiredCapabilities
from selenium.webdriver.remote import webelement , command

# outil d'automatisation de recherche
driver_location = "C:\\Users\\Frede\\OneDrive\\Bureau\\les repositorys\\AIOLIV\\chromedriver.exe"

# chemin du browser utilisé pour la recherche
binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location)
#adresse a utiliser pour la recherche
driver.get('https://www.gputracker.eu/fr/search/category/1/cartes-graphiques?textualSearch=rtx3080')
# time pour get
time.sleep(2)

driver.add_cookie({"name": "SESSION", "value": "NmNiODBmZGUtOTZkOC00YmFhLWJkYjItNTFiZjRiODgxNjAw"})
# time pour cookie
time.sleep(2)

#on defini un tableau vide
test=[]

# on défini les element a rechercher
# ne pas oublier de generaliser l'element
# 
#
price = driver.find_elements(By.XPATH,      '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div/a/div/div[3]/div/div/div[1]/span')
stok = driver.find_elements(By.XPATH,       '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div/div/div[2]')
nom = driver.find_elements(By.XPATH,        '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div/a/div/div[2]/h3')
link = driver.find_elements(By.XPATH,       '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div[2]/div/div/div[1]/a')
allresults = driver.find_elements(By.XPATH, '//*[@id="facet-search-results"]/div[2]/div/div/div/div/div[2]/div/div/div[1]/a')

# for l in link:
#     print(l.get_attribute('href'))

# for p in price:
#      print(p.text)
#      print(':)')
# print(allresults)

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
