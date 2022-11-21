
new_set = set()
with open('./wnacg_total_comic.txt', 'r', encoding='utf-8') as f:
    ls = f.read().split('\n')
    for i in ls:
        new_set.add(i)
print(len(new_set))
with open('./123.txt', 'a', encoding='utf-8') as f:
    for i in new_set:
        f.write(i+'\n')