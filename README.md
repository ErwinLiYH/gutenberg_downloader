# Data processing workshop Ⅱ group project

This repository include all code written by Erwin(kylis) for this group project

## 1. data_collect.py

download and update English txt resource from http://www.gutenberg.org/ebooks/search/?sort_order=release_date

### usage

please read help by following code:

```shell
python data_collect.py -h
python data_collect.py download -h
python data_collect.py update -h
python data_collect.py merge -h
python data_collect.py clean -h
```

please use update after download command !!!!

### example

A example workflow of data collect and process

#### download:

![](./statics/img/e1.png)

the content in conf file means the files in localhost is from 64079 to 64094.

#### update:

we delete the 64094 and modify the conf file to “64093*64079”, than update it

![](./statics/img/e2.png)

#### clean:

the picture is not updated, the argument -s should be ‘SPACE’ or ‘TAB’, not ‘ ’.

![](./statics/img/e3.png)

the 64079.txt in downPATH is:

![](./statics/img/e4.png)

the 64079.txt in out_by_SPACE is:

![](./statics/img/e5.png)

#### merge

![](./statics/img/e6.png)

## 2. mapreduce_python

the text file should have format like: id\<TAB\>content

```shell
cat merge.txt | python3 mapper.py | sort | reducer.py > result.txt
```

part of result.txt:

```
a	64060:71,64061:136,64063:71,64064:148,64068:340,64069:434,64070:1363,64071:113,64072:156,64073:248,64074:754,64075:71,64076:71,64077:187,64078:322,64079:1028,64080:71,64081:71,64082:71,64083:804,64088:698
aat	64083:1
ab	64069:3
abaco	64070:1
abaet	64068:1
abandon	64069:1,64070:2,64071:1,64083:1
abandoned	64061:1,64068:1,64069:3,64070:4,64079:1,64083:1
abandoning	64069:1,64079:1
abandonment	64068:1,64079:1
abasgians	64069:1
abashed	64083:1
abashes	64083:1
abated	64070:1
abbats	64069:1
abbey	64069:1,64079:1
```

## 3. tfidf

Check the help:

```python3
python search.py -h
```

the searched file should have format like: id\<space\>content

search.py only can run in linux who use “python3” to run python, like debian base linux.

![](./statics/img/e7.png)

output format: key_word,file_id tf-idf