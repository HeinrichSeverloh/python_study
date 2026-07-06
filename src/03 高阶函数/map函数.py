"""
4.2.1 map函数(python3)
map() 函数用于将一个函数应用到一个可迭代对象的每个元素上，并返回一个迭代器。
"""

list1 = [1, 2, 3, 4, 5]

def func(x):
    return x ** 2

result = map(func, list1)
print(result)  # 输出: <map object at 0x...>
print(list(result))  # 输出: [1, 4, 9, 16, 25]
