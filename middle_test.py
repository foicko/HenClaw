import aiohttp
import asyncio
import aiofiles
from urllib.request import getproxies
import bs4

# async def get_download_Page(_url):
#     href = _url.replace('photos', 'download')
#     html = await get_htmlAsync(href)
#     print(html)
#     soup = bs4.BeautifulSoup(await get_htmlAsync(href), 'lxml')
#     # print(soup)
#     # ls = soup.find_all('a')
#     # print(ls)

# async def get_htmlAsync(_url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(_url, proxy=getproxies()['http']) as resp:
#             return await resp.text()



# async def writeDiff2tol():
#     async with aiofiles.open('wnacg_total_comic.txt', 'a+', encoding='utf-8') as f:
#         ls = await f.read(0)
#         print(ls)
   


# asyncio.run(writeDiff2tol())


# # 下载
print(getproxies())