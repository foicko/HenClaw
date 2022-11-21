
import asyncio
import aiohttp
import aiofiles
import bs4
from urllib.request import getproxies
import time


# 去重
async def unique_file():
    async with aiofiles.open('./total.txt', 'a+', encoding='utf-8') as f:
        ls_a = await f.read()
        async for i in f:
            print(i)
        print(ls_a) 


async def get_htmlAsync(_url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(_url, proxy=getproxies()['https']) as resp:
                return await resp.text()
    except:
        print("something error")

# 获取所有套图的磁力链接
async def get_1_url(uri):
    base_head = 'https://w227k.monster/pw/'
    tol_ls = []
    new_page = base_head + uri
    text = await get_htmlAsync(new_page)
    soup = bs4.BeautifulSoup(text, 'lxml')
    divs = soup.find_all('div')
    for t in divs:
        if t.a is not None:
            if t.a.get('href') is not None:
                a = t.a.get('href')
                if len(a) > 61:
                    tol_ls.append('magnet:?xt=urn:btih:' + a[-40:])
    return tol_ls

async def write2files(urls_list, des_location):
    async with aiofiles.open(des_location, 'a+', encoding='utf-8') as f:
        for i in urls_list:
            await f.write(i+'\n')

async def get_href(uri):
    hrefs = []
    text = await get_htmlAsync(uri)
    soup = bs4.BeautifulSoup(text, 'lxml')
    trs = soup.find_all('tr')
    for i in trs:
        if i.h3 is not None:
            hrefs.append(i.h3.a.get('href'))
            # print(i.h3.a.get('href')+'\n')
    return hrefs

# 获取beg到end页码的所有网页中的单一套图链接
async def get_all_Pages(beg,end):
    fetch_array = []
    for i in range(beg,end):
        url = 'https://w227k.monster/pw/thread.php?fid=220&page='+str(i)
        fetch_array.append(get_href(url))
    return await asyncio.gather(*fetch_array)

       
async def main_Thread():
    beg_time = time.time()
    fetch2get = []
    all_pages = await get_all_Pages(8, )
    for page in all_pages:
        for one in page:
            fetch2get.append(get_1_url(one))
    mangs = await asyncio.gather(*fetch2get)
    sync_array = []
    for i in mangs:
        for mang in i:
            sync_array.append(mang)
    await write2files(sync_array, './final_file2Save'+'.txt')
    print('耗时为'+str(round(time.time()-beg_time, 3))+'s')

asyncio.get_event_loop().run_until_complete(main_Thread())
