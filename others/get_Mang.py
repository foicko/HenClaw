import requests
import re
import pymssql
import bs4
import requests

proxies = {'http': "127.0.0.1:7890",
           'https': "127.0.0.1:7890"}

base_url = 'https://s11.7086xz.xyz/pw/thread.php?fid=220'


def get_html(_url):
    r = requests.get(_url, proxies=proxies)
    r.encoding = 'utf-8'
    return r.text


# 初步获取每个网页的链接
# ls = []
# for page in range(1, 16):
#     html_content = ''
#     if page == 1:
#         html_content = get_html(base_url)
#     else:
#         html_content = get_html(base_url + '&page=' + str(page))
#     soup = bs4.BeautifulSoup(html_content, 'lxml')
#     trs = soup.find_all('tr')
#     for i in trs:
#         ls.append(i.h3)
#
# with open('only_urls.txt', 'a+', encoding='utf-8') as f:
#     for i in ls:
#         if i is not None:
#             f.write(str(i.a.get('href')) + '\n')

# 去重
div_set = set()

base_head = 'https://s11.7086xz.xyz/pw/'
ls = []
with open('only_urls.txt', 'r+', encoding='utf-8') as f:
    ls = f.read().split('\n')
#
#
tol_ls = []
#
for i in ls:
    with open('Mang_getUrl.txt', 'w+', encoding='utf-8') as f:
        new_page = base_head + i
        text = get_html(new_page)
        soup = bs4.BeautifulSoup(text, 'lxml')
        divs = soup.find_all('div')
        for t in divs:
            if t.a is not None:
                if t.a.get('href') is not None:
                    a = t.a.get('href')
                    if len(a) > 61:
                        tol_ls.append(a)
                        print(a)
                        f.write('magnet:?xt=urn:btih:' + a[-40:] + '\n')

