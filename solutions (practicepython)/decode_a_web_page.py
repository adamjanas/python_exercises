import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text)
title = soup.findAll('link')
for row in title:
     ttl_lst.append(row)

print(ttl_lst)
