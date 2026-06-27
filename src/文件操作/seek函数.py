"""
seek() 函数用于移动文件指针到指定位置。

语法：
文件.seek(偏移量, 起始位置)

起始位置：
0 - 文件开头
1 - 当前位置
2 - 文件结尾
"""

f = open("documents/test.txt", "r+")

f.seek(2, 0)  # 移动到文件开头后的第2个字节

content = f.read()
print(content)

f.close()