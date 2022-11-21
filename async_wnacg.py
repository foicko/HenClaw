# 使用协程优化爬虫效率
# 并改善用户使用体验
# mode: 1:cosplay, 2:漫画， 3:搜索模式，并提供一个额外的参数
import time
import aiohttp
import re
import bs4
import datetime
import asyncio
import aiofiles
from urllib.request import getproxies
# 主网址
base_url = 'http://www.wnacg.org'
search_url = 'http://www.wnacg.org/search/?q='


async def get_all_pages(begin, end, mode):
    ls = []
    if mode == 2:
        cate = '-cate-1.html'
    if mode == 1:
        cate = '-cate-3.html'
    for i in range(begin, end):
        url = base_url + '/albums-index-page-' + str(i) + cate
        if i == 1:
            url = base_url + '/albums-index'+cate
        ls.append(get_one_Page(url))
    return await asyncio.gather(*ls)


async def get_all_pages_Search(begin, end, param):
    ls = []
    for i in range(begin, end):
        url = base_url + f'/search/index.php?q={param}&p={str(i)}.html'
        ls.append(get_one_Page(url))
    return await asyncio.gather(*ls)


async def get_one_Page(_url):
    collections = dict()
    soup = bs4.BeautifulSoup(await get_htmlAsync(_url), 'lxml')
    ls = soup.find_all('li', class_="li gallary_item")
    for i in ls:
        collections[i.a.get("href")] = i.a.get("title")
    return collections


async def get_download_Page(_url):
    href = _url.replace('photos', 'download')
    flag = int(0)
    while flag < 100:
        html = await get_htmlAsync(href)
        if html is not None:
            break
    patten = r'<a class="down_btn ads" href="(.*?)">'
    try:
        middle = re.findall(patten, html)
        ls = middle[0]
    except:
        print('Error with middle = '+str(middle))
        print('the html is :'+html)
        ls = ''
    return 'https:' + ls


async def get_htmlAsync(_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(_url, proxy=getproxies()['https']) as resp:
            await asyncio.sleep(99)
            return await resp.text()


async def getTotal():
    async with aiofiles.open('wnacg_total_comic.txt', 'r', encoding='utf-8') as f:
        ls = await f.read()
        return ls.split('\n')


async def writeDiff2tol(urls_list):
    async with aiofiles.open('wnacg_total_comic.txt', 'a+', encoding='utf-8') as f:
        ls = await getTotal()
        # print(ls)
        for i in urls_list:
            if i in ls:
                pass
            else:
                await f.write(i+'\n')


async def normal_download(base_url, begin, end, mode=1):
    file_name = str(datetime.datetime.now()).replace(
        ' ', '_').replace(':', '_').split('.')[0]
    all_pages = await get_all_pages(begin, end, mode)
    final_ls_to_fetch = []
    for i in all_pages:
        for j in i:
            final_ls_to_fetch.append(get_download_Page(base_url + j))
    urls_list = await asyncio.gather(*final_ls_to_fetch)
    await write2files(urls_list, file_name+'.txt')
    await writeDiff2tol(urls_list)


async def search_download(beg, end, param):
    file_name = str(datetime.datetime.now()).replace(
        ' ', '_').replace(':', '_').split('.')[0]
    all_pages = await get_all_pages_Search(beg, end, param)
    final_ls_to_fetch = []
    for i in all_pages:
        for j in i:
            final_ls_to_fetch.append(get_download_Page(base_url + j))
    urls_list = await asyncio.gather(*final_ls_to_fetch)
    await write2files(urls_list, file_name+'.txt')


async def write2files(urls_list, des_location):
    async with aiofiles.open(des_location, 'a+', encoding='utf-8') as f:
        for i in urls_list:
            await f.write(i+'\n')


async def main_thread(beg, end):
    print('请选择模式: (1:Cosplay, 2:Comic, 3:Search_Mode)')
    mode_number = input()
    if mode_number == '1':
        beg_time = time.time()
        await normal_download('http://www.wnacg.org', beg, end, 1)
    if mode_number == '2':
        beg_time = time.time()
        await normal_download('http://www.wnacg.org', beg, end, 2)
    if mode_number == '3':
        print('请输入搜索的关键字：')
        param = input()
        beg_time = time.time()
        await search_download(beg, end, param=param)
    print('Finished.')
    print('耗时为'+str(round(time.time()-beg_time, 3))+'s')


def KissMe():
    beg = int(input("请输入开始页数\n"))
    end = int(input("请输入结束页数\n"))
    asyncio.run(main_thread(beg, end))
