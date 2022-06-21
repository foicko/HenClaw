with open('Mang_getUrl.txt', 'r+', encoding='utf-8') as f:
    ls = f.read().split('\n')
f.close()
ls_set =set()
for i in ls:
    ls_set.add(i)
with open('torrent.txt', 'w+', encoding='utf-8') as f:
    for i in ls_set:
        f.write('magnet:?xt=urn:btih:' + i[-40:] + '\n')
