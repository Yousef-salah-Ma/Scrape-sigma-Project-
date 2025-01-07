import requests as req
from bs4 import BeautifulSoup as bs
import csv

response = req.get('https://www.sigma-computer.com/search?search=laptop&submit_search=&route=product%2Fsearch')

soup = bs(response.text, 'html.parser')

desc = soup.find_all('div', attrs={'class': 'product-layout col-lg-15 col-md-4 col-sm-6 col-xs-12'})

url_link = []
for i in range(len(desc)):
    url_link.append('https://www.sigma-computer.com/' + desc[i].find('a')['href'])

title = []
for i in range(len(desc)):
    title.append(desc[i].find('a')['title'])

price_new = []
for i in range(len(desc)):
    price_new.append(desc[i].find('span', attrs={'class': 'price-new'}).text)

price_old = []
for i in range(len(desc)):
    price_old.append(desc[i].find('span', attrs={'class': 'price-old'}).text)

descriptions = soup.find_all('div', {'class': 'description'})
strong = []
for i in range(len(descriptions)):
    strong_tag = descriptions[i].find('strong')
    if strong_tag:
        strong.append(strong_tag.text)
    else:
        strong.append(None)

header = ['URL', 'Title', 'Price New', 'Price Old', 'Strong Description']

with open('products.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header) 
    for i in range(len(desc)):
        writer.writerow([url_link[i], title[i], price_new[i], price_old[i], strong[i]])

print("Data has been saved to 'products.csv'")
