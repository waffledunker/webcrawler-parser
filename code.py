import requests
import urllib.request
import urllib3
import time
from bs4 import BeautifulSoup,Comment #soup
import re #regex
import json
import pandas as pd #dataframe


#variables
main_url = 'https://data.ibb.gov.tr'
sort_recent_url = '/dataset?sort=views_total+desc&page='
webpage_counter = [1,2,3,4,5,6,7,8,9,10]
categories_url = '?groups='
sort_url = '?sort=views_recent+desc'
categories = ['ulasim-hizmetleri','cevre-hizmetleri','yasam','enerji-hizmetleri','guvenlik','sosyal-hizmetler','ekonomi','yonetisim']
response_arr = []
links = []


'''
def scrape_all_links():
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

#create file in pwd
    f = open("ibb_links.txt","a")

    for each in links:
        each = str(each)
        x = r.search(each,re.IGNORECASE)
        if x:
            print('link is {}'.format(x.group(1,2)))
            #write all links to a file to read it from later
            f.write('{}'.format(x.group(1)))
            f.write(' {}\n'.format(x.group(2)))
    f.close()

#first part has ended

   #get links
scrape_all_links()
'''

def data_parser():
    #variable
    url = ""

    #open file and download links one by one
    regex = re.compile('(\/dataset/.*?)\s(.*)')

    with open("ibb_links.txt","r") as fd:
        for line in fd:
            l = regex.search(line).group(1)
            ext = regex.search(line).group(2)

            #get every url(json and xml) they have on their site will be downloaded to examine later
            if ext == 'xlsx' or ext == 'json':
                url = main_url + l
                #deep dive into download links
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                download_links = soup.findAll('a',{'class':'btn-dwnld'})
                download_links = str(download_links)

                #open file to write download links inside
                regex_download = re.compile('.*href=\"(.*)\"\stitle(.*)')
                download_links = regex_download.search(download_links).group(1)

                if len(download_links.encode('utf-8',errors='replace')) > 0:
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    c = urllib3.PoolManager()

                #range of linecount of the pre-created file
                    for i in range(sum(1 for line in open('ibb_links.txt'))):
                        data = c.request('GET',download_links)
                        final_data = data.read()
                        print(final_data)
                        #time.sleep(0.5)
                        print('{} is downloaded and saved to your pwd.'.format(download_links))
                
            

        

data_parser()
