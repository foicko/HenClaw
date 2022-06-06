import requests
import re
import pymssql
import bs4
import datetime

base_url = 'http://www.wnacg.org/'


def get_html(_url):
    return requests.get(_url).text


cosplay = 'http://www.wnacg.org//albums-index-cate-3.html'


def get_table(begin, end):
    ls = []
    for i in range(begin, end):
        url = 'http://www.wnacg.org//albums-index-page-' + str(i) + '-cate-3.html'
        if i == 1:
            url = 'http://www.wnacg.org//albums-index-cate-3.html'
        ls.append(get_onePage(url))
    return ls


def get_onePage(_url):
    collections = dict()
    soup = bs4.BeautifulSoup(get_html(_url), 'lxml')
    ls = soup.find_all('li', class_="li gallary_item")
    for i in ls:
        # print(i.a.get("href"))
        # print(i.a.get("title"))
        collections[i.a.get("href")] = i.a.get("title")
    return collections


page_url = 'http://www.wnacg.org//photos-index-aid-146093.html'


def get_downloadPage(_url):
    href = _url.replace('photos', 'download')
    # print(href)
    html = get_html(href)
    patten = r'<a class="down_btn ads" href="(.*?)">'
    ls = re.findall(patten, html)[0]
    return 'https:' + ls


def main_thread():
    file_name = str(datetime.datetime.now()).replace(' ', '_').replace(':', '_').split('.')[0]
    with open('../total.txt', 'a+', encoding='utf-8') as f:
        f.seek(0)
        ls = f.read().split('\n')
        print(ls)
        print(len(ls))
        ps = get_table(1, 5)
        for i in ps:
            for j in i:
                Made_In_Heaven = get_downloadPage(base_url + j)
                if Made_In_Heaven in ls:
                    break
                else:
                    print(Made_In_Heaven)
                    with open('./txts/' + file_name + '.txt', 'a+', encoding='utf-8') as fs:
                        fs.write(Made_In_Heaven)
                        fs.write('\n')
                        f.write(Made_In_Heaven)
                        f.write('\n')


main_thread()
