name_list = ['Tom', 'Lily', 'Rose']

name_list.append('xiaoming')

name_list.extend(['xiaohong','xiaogang'])

name_list.insert(5,'xiaohuang')

i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
