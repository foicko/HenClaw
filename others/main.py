import datetime
#import requests
# import re
# import torch
#
# print(torch.cuda.is_available())
#
# base_url = 'https://www.hentaicomic.org/'
# Tonren = 'https://www.hentaicomic.org/albums-index-cate-5.html'
# cosplay = 'https://www.hentaicomic.org/albums-index-cate-3.html'
# cos2 = 'https://www.hentaicomic.org/albums-index-page-' + str(2) + '-cate-3.html'
# kern = 'https://www.hentaicomic.org/albums-index-cate-19.html'
#
#
# def get_html(_url):
#     return requests.get(_url).text
#
# def get_onePage():
#
#
#
# def get_table(begin, end):
#     for i in range(begin, end):
#         url = 'https://www.hentaicomic.org/albums-index-page-' + str(i) + '-cate-3.html'
#         if i == 1:
#             url = 'https://www.hentaicomic.org/albums-index-cate-3.html'
#

# ks = [1, 1, 1, 1, 1]
# ls = [1, 2, 3, 4, 5]
# ls[::-2] = ks[::2]
# print(ls)
# ls = "11010101010"
# qs = "10100010101"
# ks = []
# for i in range(len(ls)):
#     ks.append(ls[i] == qs[i])
#
# res = []
# score = 0
# for i in range(len(ls)):
#     if ks[i]:
#         res.append(ls[i])
#         score = score + 1
#     else:
#         res.append('X')
#
# res = ''.join(res[:])
# print(res)
# print(score)

# 去重
# set_ls = set()
# with open('./first.txt', 'r+', encoding='utf-8') as f:
#     ls = f.read().split("\n")
#     for i in ls:
#         if 'XiuRen' not in i:
#             set_ls.add(i)
#     print(len(ls))
#     set_ls = sorted(set_ls)
#     print(len(set_ls))

# with open('./total.txt', 'r+', encoding='utf-8') as f:
#     set_ls = f.read().split('\n')
#     for i in set_ls:
#         print(i)
file_name = str(datetime.datetime.now()).replace(' ', '_').replace(':', '_').split('.')[0]
print(file_name)
