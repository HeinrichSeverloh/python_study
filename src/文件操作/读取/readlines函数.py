"""
readlines() 函数用于从文件中读取所有行，返回一个列表，其中每个元素是一行内容（包括换行符）。
"""

f = open("documents/test.txt", "r")
content = f.readlines()
# 打印每一行内容
print(content)
f.close()