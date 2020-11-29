# Author: Erwin
# info: download and update txt resourse from http://www.gutenberg.org/ebooks/search/?sort_order=release_date
# last modify: 2020/11/26

import requests
from bs4 import BeautifulSoup

download_PATH='./download_PATH' # default download path