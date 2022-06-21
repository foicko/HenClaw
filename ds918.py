import requests
import re
import bs4
import datetime

# 主网址
base_url = 'http://www.wnacg.org'
search_url = 'http://www.wnacg.org/search/?q='


def get_html(_url):
    return requests.get(_url).text


cosplay = base_url + '/albums-index-cate-3.html'  # cosplay
single_book = base_url + '/albums-index-cate-6.html'  # 单行本


def get_table(begin, end):
    ls = []
    for i in range(begin, end):
        url = base_url + '/albums-index-page-' + str(i) + '-cate-3.html'
        if i == 1:
            url = base_url + '/albums-index-cate-3.html'
        ls.append(get_onePage(url))
    return ls


def get_onePage(_url):
    collections = dict()
    soup = bs4.BeautifulSoup(get_html(_url), 'lxml')
    ls = soup.find_all('li', class_="li gallary_item")
    for i in ls:
        collections[i.a.get("href")] = i.a.get("title")
    return collections


def get_downloadPage(_url):
    href = _url.replace('photos', 'download')
    # print(href)
    html = get_html(href)
    patten = r'<a class="down_btn ads" href="(.*?)">'
    middle = re.findall(patten, html)
    print(middle)
    ls = middle[0]
    return 'https:' + ls


def main_thread(beg=6, end=16):
    file_name = str(datetime.datetime.now()).replace(' ', '_').replace(':', '_').split('.')[0]
    with open('total.txt', 'a+', encoding='utf-8') as f:
        f.seek(0)
        ls = f.read().split('\n')
        print(len(ls))
        ps = get_table(beg, end)
        print(ps)
        for i in ps:
            for j in i:
                Made_In_Heaven = get_downloadPage(base_url + j)
                if Made_In_Heaven in ls:
                    print('已存在')
                    # break
                else:
                    print(Made_In_Heaven)
                    with open('./txts/' + file_name + '.txt', 'a+', encoding='utf-8') as fs:
                        fs.write(Made_In_Heaven)
                        fs.write('\n')
                        f.write(Made_In_Heaven)
                        f.write('\n')


main_thread()
# 以下为搜索下载
# search_key = '摇摇乐'
# ps = get_onePage('http://www.wnacg.org/search/?q='+search_key)
# if len(ps) == 0:
#     print('None')
# for i in ps:
#     Made_In_Heaven = get_downloadPage(base_url + i)
#     print(Made_In_Heaven)
print('finished!')
