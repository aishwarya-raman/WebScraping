from bs4 import BeautifulSoup
from datetime import datetime, time
import requests            
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
url = "https://www.fireeye.com/blog/threat-research.html"
html_page = requests.get(url, headers=headers)
soup = BeautifulSoup(html_page.content, 'lxml')
f = open("internal_links.txt", "r")
urls = []
for line in f :
    urls.append(line.strip()) 
begin_time = 12
end_time=00
def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
            a = soup.find('div', {'class':'c11v9'}).findAll('a')
            # od = soup.find('time',{'class':'entry-date'}).get('content')
            ll = "https://www.fireeye.com"+a[0].attrs['href']
            html_page = requests.get(ll, headers=headers)
            soup3 = BeautifulSoup(html_page.content, 'lxml')
            ls = soup3.find('time',{'class':'entry-date'})
            nd = ls.get('content')
            for i in urls : 
                while(i != ll) :
                   # print(i)
                    html_page = requests.get(i, headers=headers)
                    soup2 = BeautifulSoup(html_page.content, 'lxml')
                    pp = soup2.find('time',{'class':'entry-date'})
                    if(nd != pp.get('content')): 
                        print("OLD"+pp.get('content'))
                        print("NEW"+nd)
                        print(i)
                        print(ll)                   
                        print("Its updated")
                    return print("New link Updated")
                
    else: #Over midnight

        return nowTime >= startTime or nowTime <= endTime
isNowInTimePeriod(10,11,1300)