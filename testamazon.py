
import xlsxwriter

from bs4 import BeautifulSoup

from selenium import webdriver


# Generer une url à partir d'un mot clef
def get_url(search_term):
    
    # Template d'url de recherche, on remplace l'agurment get par le search_term
    template = 'https://www.amazon.com/s?k={}&sprefix=rtx+%2Caps%2C149&ref=nb_sb_ss_ts-doa-p_1_4'
    # réecrit la chaîne de caractère 'rtx + 3080'
    search_term = search_term.replace(' ', '+')

    # reformate l'url
    url = template.format(search_term)

    # Ajoute la possibilité de parcourir des pages si présentes en url
    url += '&page{}'

    return url
        
# Fonction pour extraire le nom d'un produit
def extract_nom(item):
    # Récupération de la valeur de la balise "a" présente dans l'arborescence ci dessous
    atag = item.h2.a

    # Récuperation du titre du produit
    titre  = atag.text

    string = titre

    specificité = "3080"

    if specificité in (" " + string + " "):
       
        return titre
    else:
        atag = item.h2.a
        titre  = atag.text.strip()
        string = titre

def extract_url(item):

    atag = item.h2.a

    # description  = atag.text.strip()

    titre  = atag.text

    string = titre

    specificité = "3080"

    if specificité in (" " + string + " "):
       
        # description et url 
        url = 'https://www.amazon.com' + atag.get('href')
        return url
    else:
        atag = item.h2.a
        titre  = atag.text.strip()
        string = titre

def extract_prix(item):
    atag = item.h2.a

    # description  = atag.text.strip()

    titre  = atag.text

    string = titre

    specificité = "3080"

    if specificité in (" " + string + " "):
        try:
            # prix
            price_parent = item.find('span', 'a-price')


            prices = price_parent.find('span', 'a-offscreen').text

            return prices

        except AttributeError:
            return
        
    else:
        atag = item.h2.a
        titre  = atag.text.strip()
        string = titre

# Création du programme à lancer
def main(search_term):
    # Démarrer le webdriver
    driver = webdriver.Chrome()

    listeNom = []
    listeUrl = []
    listePrix = []

    
    url = get_url(search_term)

    for page in range(1, 3):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            nomProduit = extract_nom(item)
            urlProduit = extract_url(item)
            prixProduit = extract_prix(item)
            if nomProduit:
                listeNom.append(nomProduit)
                listePrix.append(prixProduit)
                listeUrl.append(urlProduit)
                
            # if url:
            #     records.append(url)

                
    
    driver.close()

    array = []

    for i in range(len(listeNom)):
        array.append(listeNom[i])
        array.append(listePrix[i])
        array.append(listeUrl[i])

    return array
        
    # print(Produit)
    # workbook = xlsxwriter.Workbook('Amazon.xlsx')

    # worksheet = workbook.add_worksheet()

    # row = 0
    # column = 0

    # for data in array:
    #     if row == 0:
    #         worksheet.write(row, column, 'NOM')
    #         column += 1 
    #         worksheet.write(row, column, 'PRIX')
    #         column += 1 
    #         worksheet.write(row, column, 'LIEN')
    #         column = 0 
    #         row += 1

    #     worksheet.write(row, column, data)
    #     column += 1 
        
    #     if column == 3:
    #         column = 0
    #         row += 1

    
    # workbook.close() 

