import requests
import re
import pymssql
import bs4
import datetime

proxies = {'http': "127.0.0.1:7890",
           'https': "127.0.0.1:7890"}

base_url = 'https://s11.7086xz.xyz/pw/thread.php?fid=220'


# base_url = 'https://www.codeleading.com/'


def get_html(_url):
    r = requests.get(_url, proxies=proxies)
    r.encoding = 'utf-8'
    return r.text


# soup = bs4.BeautifulSoup(get_html(base_url), 'lxml')
# ls = soup.find_all('tr')
#
# for i in ls:
#     print(i.h3)

ls = []
for page in range(1, 16):
    html_content = ''
    if page == 1:
        html_content = get_html(base_url)
    else:
        html_content = get_html(base_url + '&page=' + str(page))
    soup = bs4.BeautifulSoup(html_content, 'lxml')
    trs = soup.find_all('tr')
    for i in trs:
        ls.append(i.h3)

with open('only_urls.txt', 'a+', encoding='utf-8') as f:
    for i in ls:
        if i is not None:
            f.write(str(i.a.get('href')) + '\n')
print(ls)
