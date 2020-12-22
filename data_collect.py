# Author: Erwin
# info: download and update English txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date
# last modify: 2020/12/01
# ---------------------------------------------------------------------------------------------------------------------------------------------------
import re
import os
import sys
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
    latest_index = int(links[0].split('/')[-1])
    strindex = -1
    try:
        with open(confPATH,'r') as f:
            strindex = f.readline()
    except:
        pass
    if strindex==-1:
        big_index=-1
        small_index=-1
    else:
        big_index=int(strindex.split('*')[0])
        small_index=int(strindex.split('*')[1])
    return latest_index,big_index,small_index

def download_ebook_size(args):
    size=args.size
    path=args.path
    sleep_time=args.s
    if path.endswith('/') or path.endswith('\\'):
        downPATH = path + 'downPATH'
    else:
        downPATH = path+'/'+ 'downPATH'
    if path.endswith('/') or path.endswith('\\'):
        confPATH = path + 'conf'
    else:
        confPATH = path+'/'+ 'conf'

    url='http://www.gutenberg.org/ebooks/search/?sort_order=release_date'
    latest_index,big_index,small_index = check_update(url,path)
    if small_index==-1:
        index=latest_index
        big_index=latest_index
    elif small_index!=-1:
        index=small_index-1

    if os.path.exists(downPATH) == False:
        os.mkdir(downPATH)
    else:
        a = input('Warning: Do you want to go on dowload begin %d? Y/n'%(index))
        if a == 'y' or a == 'Y' or a == '':
            pass
        elif a == 'n' or a == 'N':
            return
        else:
            return
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
    with open(confPATH,'w') as conf:
        conf.write('%d*%d'%(big_index,index+1))
    print('Finish, size: %0.3f'%folder_size(downPATH))

def update(args):
    path = args.path
    sleep_time = args.s
    if path.endswith('/') or path.endswith('\\'):
        downPATH = path + 'downPATH'
    else:
        downPATH = path+'/'+ 'downPATH'
    if path.endswith('/') or path.endswith('\\'):
        confPATH = path + 'conf'
    else:
        confPATH = path+'/'+ 'conf'
    if os.path.exists(downPATH) == False:
        os.mkdir(downPATH)
    url='http://www.gutenberg.org/ebooks/search/?sort_order=release_date'
    latest_index,big_index,small_index = check_update(url,path)
    if latest_index == big_index:
        print('all things are up to date')
        return
    header={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    for ind_ex in range(big_index+1,latest_index+1):
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
    big_index=latest_index
    with open(confPATH,'w') as conf:
        conf.write('%d*%d'%(big_index,small_index))

def merge(args):
    path = args.path

    li = os.listdir(path)
    with open(path+'/merge.txt','a') as me:
        for txt_file in li:
            with open(path+'/'+txt_file,'r') as f:
                me.write(f.read()+'\n')

def extract_words(string):
    b=re.compile(r'[a-z]+', re.I).findall(string)
    s=''
    for i in b:
        s+=(i+' ')
    return s

def clean(args):
    inp_folder=args.input
    out_folder=args.output
    split=args.s

    if inp_folder.endswith('/') or inp_folder.endswith('\\'):
        inp_folder = inp_folder[0:-1]

    if out_folder.endswith('/') or out_folder.endswith('\\'):
        out_folder = out_folder[0:-1]

    if inp_folder==out_folder:
        raise Exception("inupt and out put can't be same!!!")
    if os.path.isdir(inp_folder)==False:
        raise Exception('input sholud be a folder!!!')
    if os.path.isdir(out_folder)==False:
        raise Exception('output shold be a folder!!!')
    files = os.listdir(inp_folder)
    for fil_e in files:
        i_d=fil_e.split('.')[0]
        with open('%s/%s'%(inp_folder,fil_e),'r') as inp:
            s=extract_words(inp.read())
            with open('%s/%s'%(out_folder,fil_e),'w') as out:
                out.write(i_d+split+s)

class temp:
    pass

def merge_for_import(path):
    args = temp()
    args.path = path
    merge(args)

def download_ebook_size_for_import(path,size,sleep_time):
    args = temp()
    args.path = path
    args.size = size
    args.s = sleep_time
    download_ebook_size(args)

def update_for_import(path,sleep_time):
    args = temp()
    args.path = path
    args.s = sleep_time
    update(args)

if __name__ == "__main__":
    import argparse
    # parse command line arguments
    main_parser = argparse.ArgumentParser(description='Download and update English txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date')
    sub_parser = main_parser.add_subparsers()

    # download subcommand
    download_ebook_size_sub = sub_parser.add_parser('download',description='Download ebooks by size to downPATH')
    download_ebook_size_sub.add_argument('path',type=str,help='project path, namely, the parent path of "downPATH" folder')
    download_ebook_size_sub.add_argument('size',type=float,help='the least size you want')
    download_ebook_size_sub.add_argument('-s',type=int,metavar='sleep_time',default=5,help='the time gaps between two requests')
    download_ebook_size_sub.set_defaults(func=download_ebook_size)

    # update subcommand
    update_sub = sub_parser.add_parser('update',description='download laest ebooks to downPATH')
    update_sub.add_argument('path',type=str,help='project path, namely, the parent path of "downPATH" folder')
    update_sub.add_argument('-s',type=int,metavar='sleep_time',default=5,help='the time gaps between two requests')
    update_sub.set_defaults(func=update)

    # merge subcommand
    merge_sub = sub_parser.add_parser('merge',description='merge all the txt file in path to merge.txt')
    merge_sub.add_argument('path',type=str,help='the path of folder caontains all text file you want to merge')
    merge_sub.set_defaults(func=merge)

    clean_sub = sub_parser.add_parser('clean',description='extract words of all text data')
    clean_sub.add_argument('input',type=str,help='the parent path of text file')
    clean_sub.add_argument('output',type=str,help='the output path')
    clean_sub.add_argument('-s',metavar='split char',type=str,help='the split char between id and content',default='\t')
    clean_sub.set_defaults(func=clean)

    args = main_parser.parse_args(sys.argv[1:])
    # print(args)
    args.func(args)