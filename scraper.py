import requests
from bs4 import BeautifulSoup

def scrape_books():
    url = 'http://books.toscrape.com/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    books = []
    for book in soup.select('.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        books.append({'title': title, 'price': price})

    return books


print(scrape_books())