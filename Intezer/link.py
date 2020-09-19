
# Program to get intenal links
import requests
from bs4 import BeautifulSoup
import time
import sys
from urllib.request import urlparse, urljoin
               
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
url = "https://www.intezer.com/blog/"
html_page = requests.get(url, headers=headers)
soup = BeautifulSoup(html_page.content, 'lxml')

head = soup.find_all('div',class_="single-post-page")
count = 0
with open(f"internal_links.txt", "w") as f:
    for div in soup.findAll('div', {'class': 'single-post-page'}):
        if(count <5) :
            a = div.findAll('a')[1]
            print (a.attrs['href'], file=f)
            count = count +1
        else :
            break
