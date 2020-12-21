# Data processing workshop Ⅱ group project

This repository includ all code writen by Erwin(kylis) for this group project

## 1. data_collect.py

download and update English txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date

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

pwd is “/home/kylis/Desktop/git project/github/dp_project”

#### download:

<img src="./statics/img/1.png" style="zoom:40%;" />

the structure of ./test folder after “download” like following screenshot:

<img src="./statics/img/2.png" style="zoom:30%;" />

#### update:

Before update, the latest ebook is 63938.

<img src="./statics/img/after.png" style="zoom:30%;" />

Update it:

```shell
python3 update_ebook.py update ./test
```

Now the latest ebbok is 63953.

<img src="./statics/img/4.png" style="zoom:30%;" />

#### merge:

<img src="./statics/img/5.png" style="zoom:40%;" />

the structure of ./test folder after “merge” like following screenshot:

<img src="./statics/img/6.png" style="zoom:30%;" />

### clean

clean all the text file in input folder and out put to output folder

“clean” means: extract all the words in text file, and reformat it to

```
doc_id	content
#splited by \t
```

<img src="./statics/img/7.png" style="zoom:40%;" />

The 64059.txt in downPATH before clean:

<img src="./statics/img/8.png" style="zoom:20%;" />

The 64059.txt in out folder after clean:

<img src="./statics/img/10.png" style="zoom:20%;" />