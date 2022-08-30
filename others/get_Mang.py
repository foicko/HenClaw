
import asyncio
from asyncore import write
from time import sleep
import requests
import re
import bs4
import threading
proxies = {'http': "127.0.0.1:7890",
           'https': "127.0.0.1:7890"}

base_url = 'https://s11.7086xz.xyz/pw/thread.php?fid=220'
ls = []

def get_html(_url):
    r = requests.get(_url, proxies=proxies)
    r.encoding = 'utf-8'
    return r.text


 # 初步获取每个网页的链接
def get_baseUrl(page):
    litte_case = []
    if page == 1:
        html_content = get_html(base_url)
    else:
        html_content = get_html(base_url + '&page=' + str(page))
    soup = bs4.BeautifulSoup(html_content, 'lxml')
    trs = soup.find_all('tr')
    for i in trs:
        if i.h3 is not None:
            litte_case.append(i.h3.a.get('href')+'\n')
            print(i.h3.a.get('href')+'\n')
    # with open('only_urls.txt', 'a+', encoding='utf-8') as f:
    #     for i in litte_case:
    #         if i is not None:
    #             f.write(i + '\n')


def write_after(): 
    with open('only_urls.txt', 'a+', encoding='utf-8') as f:
        for i in ls:
            if i is not None:
                f.write(str(i.a.get('href')) + '\n')

def get_Mang():
    base_head = 'https://s11.7086xz.xyz/pw/'
    ls = []
    with open('only_urls.txt', 'r+', encoding='utf-8') as f:
        ls = f.read().split('\n')
    tol_ls = []
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


async def get_1_url(uri):
    base_head = 'https://s11.7086xz.xyz/pw/'
    tol_ls = []
    new_page = base_head + uri
    text = get_html(new_page)
    soup = bs4.BeautifulSoup(text, 'lxml')
    divs = soup.find_all('div')
    for t in divs:
        if t.a is not None:
            if t.a.get('href') is not None:
                a = t.a.get('href')
                if len(a) > 61:
                    tol_ls.append(a)
                    # if a is not '':
                        # print('magnet:?xt=urn:btih:' + a[-40:] + '\n')
    return tol_ls

def write_mang(ls):
    with open('Mang_getUrl.txt', 'w+', encoding='utf-8') as f:
        for a in ls:
            print(a)
            f.write('magnet:?xt=urn:btih:' + a[-40:] + '\n')


async def write_and_get():
    with open('only_urls.txt', 'r', encoding='utf-8') as f:
        litte_case = f.read().split('\n')
        for i in litte_case:
            ls = get_1_url(i)
            await asyncio.run(ls)
            write_mang(ls)
# async def main(index):
#     # for i in range(index):
#     #     th = threading.Thread(target=get_baseUrl, args=(i,))
#     #     th.start()

# asyncio.run(main(20))

# with open('only_urls.txt', 'r', encoding='utf-8') as f:
#         litte_case = f.read().split('\n')
#         for i in litte_case:
#             # print(i)
#             th = threading.Thread(target=get_1_url, args=(i,))
#             # th.start()
#             print(th.start())
#             sleep(1)
#             break
                
# write_and_get
asyncio.run(write_and_get())