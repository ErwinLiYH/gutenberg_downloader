# Data processing workshop Ⅱ group project

This repository includ all code writen by Erwin(kylis) for this group project

## 1. update_ebooks.py

download and update English txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date

### usage

please read help by following code:

```shell
python update_ebooks.py -h
python update_ebooks.py download -h
python update_ebooks.py update -h
python update_ebooks.py merge -h
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