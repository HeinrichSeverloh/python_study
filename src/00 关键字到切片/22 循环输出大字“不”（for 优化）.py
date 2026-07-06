# 定义各行：(缩进空格数, 内容)
lines = [
    (1,  "-------------"),
    (7,  "|"),
    (4,  "/  |  \\"),
    (3,  "/   |   \\"),
    (2,  "/    |    \\"),
    (7,  "|"),
]

# 统一打印
for indent, content in lines:
    print(' ' * indent + content)