from bs4 import BeautifulSoup
import requests
import json

try:
    data ={}
    data['Books'] = []
    url = 'https://books.toscrape.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'lxml')

    for idx,book in enumerate(soup.find_all('li',class_="col-xs-6"),start=1):
        bookTitle = book.find('h3')
        bookPrice = book.find('p',class_="price_color")
        bookStock = book.find('p',class_="instock availability")
        price = bookPrice.text.split('Â£')[-1]
        data['Books'].append({
            'id':idx,
            'Title':bookTitle.text,
            'Price':f'${price}',
            'Stock':bookStock.text.strip()
        })
    print(data['Books'])

    ## Escribir archivo Books.json:
    with open('Books.json','w') as file:
        json.dump(data,file)

except:
    print('There was a error, review the Code')

