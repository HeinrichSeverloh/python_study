"""
4.2.2 reduce函数(python3)
reduce() 函数用于将一个二元函数应用到一个可迭代对象的每个元素上，从左到右累积计算，最终得到一个单一的返回值。
"""

import functools as f

list1 = [1, 2, 3, 4, 5]

def func(x, y):
    return x + y

result = f.reduce(func, list1)
print(result)  # 输出: 15