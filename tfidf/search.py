# Author Erwin
# search by tf-idf
# Last modification: 10:49
# ---------------------------------------------------------------------
import argparse
import sys
import os
import re

def search(args):
    search_file=args.search
    tfidf_file=args.tfidf
    key_word=args.key_word

    os.system('cat %s | python3 Mapper1.py | sort |python3 Reducer1.py |python3 Mapper2.py | sort | python3 Reducer2.py | python3 Mapper3.py | sort | python3 Reducer3.py > %s'%(search_file,tfidf_file))
    dic={}
    with open('./%s'%tfidf_file,'r') as f:
        string=f.read()
    restr='%s,\d+\s\d.\d+'%key_word
    b=re.compile(restr, re.I).findall(string)
    for i in b:
        temp=i.split('\t')
        dic[temp[0]]=float(temp[1])
    sort_dic=sorted(dic.items(),key=lambda x: x[1],reverse=True)
    for i in sort_dic:
        print(i[0],i[1])

main_parser=argparse.ArgumentParser(description='seach text file by td-idf')
main_parser.add_argument('key_word',type=str,help='the key word you want to search')
main_parser.add_argument('-search',type=str,help='the file path you want to search, defult is ./merge.txt',default='./merge.txt')
main_parser.add_argument('-tfidf',type=str,help='the tfidf file path, defult is ./tfidf.txt',default='./tfidf.txt')
main_parser.set_defaults(func=search)

args = main_parser.parse_args(sys.argv[1:])
# print(args)
args.func(args)