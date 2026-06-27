"""
4.2.3 filter函数(python3)
filter() 函数用于过滤一个可迭代对象，返回一个迭代器，该迭代器包含满足条件的元素。
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x % 2 == 0

result = filter(func, list1)
print(result)  # 输出: <filter object at 0x...>
print(list(result))  # 输出: [2, 4, 6, 8, 10]