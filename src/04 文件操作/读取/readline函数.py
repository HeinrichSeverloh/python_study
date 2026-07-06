"""
readline() 函数用于从文件中读取一行内容，返回一个字符串，包含该行的内容（包括换行符）。
"""
f = open("documents/test.txt", "r")
content = f.readline()
print(f'第一行内容: {content}')
content = f.readline()
print(f'第二行内容: {content}')
content = f.readline()
print(f'第三行内容: {content}')
content = f.readline()
print(f'第四行内容: {content}')
content = f.readline()
print(f'第五行内容: {content}')
f.close()