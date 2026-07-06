"""
read() 函数用于从文件中读取内容。它会返回一个字符串，包含文件中的所有内容。

语法：
文件.read(num)
其中，num 是一个可选参数，表示要读取的字符数。如果省略 num 或将其设为负数，则会读取整个文件。
"""

f = open("documents/test.txt", "r")
content = f.read()
print(content)
f.close()