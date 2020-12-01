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

![](./statics/img/1.png)

the structure of ./test folder after “download” like following screenshot:

![](./statics/img/2.png)

#### update:

![](./statics/img/3.png)

![](./statics/img/4.png)

#### merge:

![](./statics/img/5.png)

the structure of ./test folder after “merge” like following screenshot:

![](./statics/img/6.png)