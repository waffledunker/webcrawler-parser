import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

main_url = 'https://data.ibb.gov.tr/dataset'
sort_recent_url = '?sort=views_recent+desc&page='
webpage_counter = [1,2,3,4,5,6]
categories_url = '?groups='
sort_url = '?sort=views_recent+desc'
categories = ['ulasim-hizmetleri','cevre-hizmetleri','yasam','enerji-hizmetleri','guvenlik','sosyal-hizmetler','ekonomi','yonetisim']
response_arr = []
links = []
datalink_arr = []

#check all categories inside website are reachable
for i in webpage_counter:
    response = requests.get(main_url + sort_recent_url + str(webpage_counter[i-1]))
    soup = BeautifulSoup(response.text, 'html.parser')
    tagfind = soup.findAll('a',text=['XML','CSV','PDF','XLSX','API','JSON'])
    for each in tagfind:
        links.append(each)
        print(each)

#get links with regex


r = re.compile('^/dataset/.*"$(>PDF|XML|XLSX|API|JSON|CSV<)')






    