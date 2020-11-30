# Author: Erwin
# info: download and update txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date
# last modify: 2020/11/26
# ---------------------------------------------------------------------------------------------------------------------------------------------------

from sys import argv
import requests
from bs4 import BeautifulSoup
from time import sleep
import os
from lxml import etree

def folder_size(path):
    return round(sum(os.path.getsize(path+'/'+f) for f in os.listdir(path))/1024/1024,3)

def check_update(url,path):
    if path.endswith('/') or path.endswith('\\'):
        confPATH = path+'conf'
    else:
        confPATH = path+'/'+'conf'
    a = requests.get(url)
    html = a.text
    soup = BeautifulSoup(html,'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    links = [link for link in links if link.startswith('/ebooks/')]
    links = [link for link in links if link.split('/')[-1].isdigit()]
    index = int(links[0].split('/')[-1])
    with open(confPATH,'r') as f:
        strindex = f.readline()
    if strindex==str(index):
        switch = False
    else:
        with open(confPATH,'w') as f:
            f.write(str(index))
        switch = True
    old_index = int(strindex)
    return index,old_index,switch

def download_ebook_size(size,path,sleep_time):
    if path.endswith('/') or path.endswith('\\'):
        downPATH = path + 'downPATH'
    else:
        downPATH = path+'/'+ 'downPATH'
    if os.path.exists(downPATH) == False:
        os.mkdir(downPATH)
    url='http://www.gutenberg.org/ebooks/search/?sort_order=release_date'
    index,oldindex,switch = check_update(url,path)
    header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    while folder_size(downPATH) <= size:
        num = 1
        while num <=3 :
            temp_requ = requests.get('http://www.gutenberg.org/ebooks/%d'%index,headers=header)
            temp_requ.encoding='utf-8'
            if temp_requ.status_code==200:
                data = etree.HTML(temp_requ.text)
                a = data.xpath('/html/body/div[1]/div[1]/div[2]/div[4]/div/div[3]/div/table/tr//*/text()')
                lan_in = a.index('Language')
                if a[lan_in+1] == 'English' or a[0]=='英语':
                    print('size: %0.3f, begin requests http://www.gutenberg.org/files/%d/%d-0.txt'%(folder_size(downPATH),index,index))
                    temp_requ = requests.get('http://www.gutenberg.org/files/%d/%d-0.txt'%(index,index),headers=header)
                    print('requests http://www.gutenberg.org/files/%d/%d-0.txt successfully'%(index,index))
                    with open(downPATH+'/'+str(index)+'.txt','wb') as txtfile:
                        txtfile.write(temp_requ.content)
                else:
                    print('%d is not English book'%index)
                sleep(sleep_time)
                index-=1
                break
            else:
                num+=1
    print('Finish, size: %0.3f'%folder_size(downPATH))

def update(path,sleep_time):
    if path.endswith('/') or path.endswith('\\'):
        downPATH = path + 'downPATH'
    else:
        downPATH = path+'/'+ 'downPATH'
    if os.path.exists(downPATH) == False:
        os.mkdir(downPATH)
    url='http://www.gutenberg.org/ebooks/search/?sort_order=release_date'
    index,oldindex,switch = check_update(url,path)
    if switch == False:
        print('all things are up to date')
        return
    header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    for ind_ex in range(oldindex+1,index+1):
        num = 1
        while num <= 3:
            temp_requ = requests.get('http://www.gutenberg.org/ebooks/%d'%ind_ex,headers=header)
            if temp_requ.status_code==200:
                data = etree.HTML(temp_requ.text)
                a = data.xpath('/html/body/div[1]/div[1]/div[2]/div[4]/div/div[3]/div/table/tr//*/text()')
                lan_in = a.index('Language')
                if a[lan_in+1] == 'English' or a[0]=='英语':
                    print('begin requests http://www.gutenberg.org/files/%d/%d-0.txt'%(ind_ex,ind_ex))
                    temp_requ = requests.get('http://www.gutenberg.org/files/%d/%d-0.txt'%(ind_ex,ind_ex),headers=header)
                    print('requests http://www.gutenberg.org/files/%d/%d-0.txt successfully'%(ind_ex,ind_ex))
                    with open(downPATH+'/'+str(ind_ex)+'.txt','wb') as txtfile:
                        txtfile.write(temp_requ.content)
                else:
                    print('%d is not English book'%ind_ex)
                sleep(sleep_time)
                break
            else:
                num+=1

download_ebook_size(5,'.',3)