# Author: Erwin
# info: download and update txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date
# last modify: 2020/11/26

from sys import argv
import requests
from bs4 import BeautifulSoup
from time import sleep
import os
from lxml import etree

def folder_size(path):
    return round(sum(os.path.getsize(path+'/'+f) for f in os.listdir(path))/1024/1024,3)

def download_ebook(size,path,sleep_time):
    downPATH = path+'/'+ 'downPATH'
    if os.path.exists(downPATH) == False:
        os.mkdir(downPATH)
    url='http://www.gutenberg.org/ebooks/search/?sort_order=release_date'
    a = requests.get(url)
    html = a.text
    soup = BeautifulSoup(html,'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    links = [link for link in links if link.startswith('/ebooks/')]
    links = [link for link in links if link.split('/')[-1].isdigit()]
    index = int(links[0].split('/')[-1])
    while folder_size(downPATH) <= size:
        print('\r'+folder_size(downPATH),end='')
        print('http://www.gutenberg.org/ebooks/%d'%index)
        temp_requ = requests.get('http://www.gutenberg.org/ebooks/%d'%index)
        data = etree.HTML(temp_requ.text)
        a = data.xpath('/html/body/div[1]/div[1]/div[2]/div[4]/div/div[3]/div/table/tr[4]/td/text()')
        if a[0] == 'English':
            temp_requ = requests.get('http://www.gutenberg.org/files/%d/%d-0.txt'%(index,index))
            with open(downPATH+'/'+str(index)+'.txt','w') as txtfile:
                txtfile.write(temp_requ.text)
        sleep(sleep_time)

download_ebook(1,'.',2)