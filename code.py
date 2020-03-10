import requests
import urllib.request
import time
from bs4 import BeautifulSoup,Comment
import re

main_url = 'https://data.ibb.gov.tr/dataset'
sort_recent_url = '?sort=views_total+desc&page='
webpage_counter = [1,2,3,4,5,6,7,8,9,10]
categories_url = '?groups='
sort_url = '?sort=views_recent+desc'
categories = ['ulasim-hizmetleri','cevre-hizmetleri','yasam','enerji-hizmetleri','guvenlik','sosyal-hizmetler','ekonomi','yonetisim']
response_arr = []
links = []

#check all categories inside website are reachable
for i in webpage_counter:
    response = requests.get(main_url + sort_recent_url + str(webpage_counter[i-1]))
    soup = BeautifulSoup(response.text, 'html.parser')
    tagfind = soup.findAll(string=lambda text: isinstance(text, Comment))
    for each in tagfind:
        #print(each)
        print("==========")
        links.append(each.extract())
        print(len(links))

#get links with regex

#r = re.compile(r'.*(\/dataset.*?)\"\s.*\"(\w+)\".*')
r = re.compile(r'.*\s\w+?\=\"(\/dataset\/.*?)\".*\sdata\-format\=\"(\w+)\".*')
for each in links:
    each = str(each)
    x = r.search(each,re.IGNORECASE)
    if x:
        print('link is {}'.format(x.group(1,2)))
    
    
#st = '<a href="/dataset/ibb-istac-araclarinin-anlik-konum-ve-hiz-bilgileri" class="label no-margin-top no-margin-bottom" data-format="csv">CSV</a>'
#x = r.search(st,re.IGNORECASE).groups(1)
#print(x)

    