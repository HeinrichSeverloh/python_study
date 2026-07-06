mystr1  = "hello world and itcast and itheima and Python"

# 1. replace() 把and换成he ** 说明replace函数有返回值，返回值是修改后的字符串
# new_str = mystr1.replace('and', 'he')
# new_str = mystr1.replace('and', 'he', 1)
# 替换次数如果超出子串出现的次数，表示替换所有这个子串
# new_str = mystr1.replace('and', 'he', 10)
# print(mystr1)
# print(new_str)

# **** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
# --- 说明 字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型

# 2. split() --- 分割，返回一个列表，丢失分割字符
# list1 = mystr1.split('and')
# list1 = mystr1.split('and', 2)
# print(list1)
# 3. join() -- 合并列表里面的字符串数据为一个大字符串
# mylist = ['aa', 'bb', 'cc']
# aa...bb...cc
# new_str = '...'.join(mylist)
# print(new_str)

# 1. capitalize() 字符串首字母大写
# new_str = mystr.capitalize()

# 2.title(): 字符串中每个单词首字母大写
# new_str = mystr.title()

# 3. upper(): 小写转大写
# new_str = mystr.upper()

# 4. lower(): 大写转小写
# new_str = mystr.lower()

# print(new_str)

mystr2 = "  hello world and itcast and itheima and Python   "
# print(mystr2)
# 1. lstrip(): 删除左侧空白字符
# new_str = mystr.lstrip()

# 2. rstrip(): 删除右侧空白字符
# new_str = mystr.rstrip()

# 3. strip(): 删除两侧空白字符
# new_str = mystr.strip()
# print(new_str)


