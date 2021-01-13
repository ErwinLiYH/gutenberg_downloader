#! /usr/bin/python
 
from sys import stdin
import re
 
for line in stdin:
        doc_id, content = line.split('\t')
 
        words = re.findall(r'\w+', content)
                 
        for word in words:
                print("%s\t%s:1" % (word.lower(), doc_id))
