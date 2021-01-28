import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'scrapeme.live',
    'dnt': '1',
    'upgrade-insecure-requests': '3',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
'Safari/537.36',
    'accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

print('_____________________________\n\n')

#Walmart
search_query = input('Enter your product name for walmart: ')
search_query = search_query.replace(" ", '-')
url="https://www.walmart.com/search/?query="+search_query
print(url)
page=requests.get(url,headers=headers)
src = page.content
soup = BeautifulSoup(src, 'lxml')
walmart_name = soup.find("a",{"class": "product-title-link line-clamp line-clamp-2 truncate-title"})
walmart_price = soup.find("span", {"class": "price-group"})
try:
    print("-----------------------\nWalmart:\n")
    if walmart_name:
        print('Product name:\n', walmart_name.text)
        print('Product price:\n',walmart_price.text)
        print("-----------------------")
    else:
        print('No product found!')
        print("-----------------------") 
except:
    print('Walmart: No product found!')
    print("-----------------------") 

# Amazon
name = input('Enter the product name for Amazon: ')
name1 = name.replace(" ", "-")
name2 = name.replace(" ", "+")
link = f'https://www.amazon.com/{name1}/s?k={name2}'
print(link)
result = requests.get(link, headers=headers)
src = result.content
soup = BeautifulSoup(src, 'lxml')
try:
    amazon_name = soup.find(
        'span', {"class": "a-size-medium a-color-base a-text-normal"})
    print('Product name:\n', amazon_name.text)
    print("----------------\nAmazon:\n")
    amazon_price = soup.find('span', {"class": "a-offscreen"})
    print('Price: ', amazon_price.text)
    print("-----------------------")

except:
    print("----------------\nAmazon:")
    print("\nAmazon: No product found!")
    print("-----------------------")    

# Newegg
name = input('Enter the product name for Newegg: ')
name1 = name.replace(" ", "+")
link = f'https://www.newegg.com/p/pl?d={name1}'
print(link)
result = requests.get(link, headers=headers)
src = result.content
soup = BeautifulSoup(src, 'lxml')
print("----------------\nBestBuy:\n")
try:
    newegg_name = soup.find(
        'a', {"class": "item-title"})
    print('Product name:\n', newegg_name.text)
    items = soup.findAll('li',attrs={"class":"price-current"})
    if len(items) > 0: 
        for item in items:
            newegg_price = item.find('strong').text
            break
    print('\nPrice: $ ', newegg_price)
    print("-----------------------")
except:
    print("\nNewegg: No product found!")
    print("-----------------------")   

print('\n______________________________________\n\n')     