#! /usr/bin/python
 
from sys import stdin
import re
 
index = {}
         
for line in stdin:
        word, postings = line.split('\t')
 
        index.setdefault(word, {}) 
                 
        for posting in postings.split(','):
                doc_id, count = posting.split(':')
                count = int(count)
 
                index[word].setdefault(doc_id, 0)
                index[word][doc_id] += count
  
for word in index:
        postings_list = ["%s:%d" % (doc_id, index[word][doc_id]) 
                         for doc_id in index[word]]
 
        postings = ','.join(postings_list)
        print('%s\t%s' % (word, postings))