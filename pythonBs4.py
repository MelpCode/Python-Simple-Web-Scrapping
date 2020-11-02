from bs4 import BeautifulSoup
import requests
import json

try:
    data = {}
    data['Quotes']=[]
    url = "https://quotes.toscrape.com/"
    r = requests.get(url)
    soup =  BeautifulSoup(r.text, 'lxml')
    tagsList = []
    #quote = soup.find('span', class_="text") #JUST ONE QUOTE
    for idx,quoteContent in enumerate(soup.find_all('div',class_="quote"),start=1):
        quote = quoteContent.find('span',class_="text")
        quoteText = quote.text.split('“')[-1].split('”')[0]
        author = quoteContent.find('small',class_="author")
        tagsList=[]
        for tags in quoteContent.find_all('a',class_="tag"):
            tagsList.append(tags.text)

        data['Quotes'].append({
            'id':idx,
            'Quote':quoteText,
            'Author':author.text,
            'Tags':', '.join(tagsList)

        })
    print(data)

    ## Guardamos los datos en una Formato JSON
    with open('Quotes.json','w') as file:
        json.dump(data,file)
except:
    print('There was a error, Review the Code')

