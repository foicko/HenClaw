# import requests
# import re
# import pymssql
# import bs4
# import datetime
#
# proxies = {'http': "127.0.0.1:7890",
#            'https': "127.0.0.1:7890"}
# base_url = 'https://s11.7086xz.xyz/pw/'
# ls = []
# with open('only_urls.txt', 'r+', encoding='utf-8') as f:
#     ls = f.read().split('\n')
#
#
# def get_html(_url):
#     r = requests.get(_url, proxies=proxies)
#     r.encoding = 'utf-8'
#     return r.text
#
#
# tol_ls = []
#
# for i in ls:
#     new_page = base_url + i
#     text = get_html(new_page)
#     soup = bs4.BeautifulSoup(text, 'lxml')
#     divs = soup.find_all('div')
#     for t in divs:
#         if t.a is not None:
#             if t.a.get('href') is not None:
#                 a = t.a.get('href')
#                 if len(a) > 61:
#                     tol_ls.append(a)
#
# with open('torrent.txt', 'w+', encoding='utf-8') as f:
#     for i in tol_ls:
#         f.write(i + '\n')


# 去重
sls = set()
# with open('ts.sh', 'r+', encoding='utf-8') as f:
#     ls = f.read().split('\n')
#     for i in ls:
#         sls.add(i)
#
# with open('torrent.txt', 'w+', encoding='utf-8') as f:
#     for i in sls:
#         f.write(i + '\n')


with open('ts.sh', 'r+', encoding='utf-8') as f:
    ls = f.read().split('\n')
    for i in ls:
        i = i[-40:]
        print(i)
        sls.add('magnet:?xt=urn:btih:'+i)

with open('torrent.txt', 'w+', encoding='utf-8') as f:
    for i in sls:
        f.write(i + '\n')