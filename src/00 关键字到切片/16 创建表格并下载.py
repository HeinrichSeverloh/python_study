import pandas as pd

# 创建表格数据
data = {
    "特性": [
        "语法逻辑",
        "循环变量",
        "适用场景",
        "代码简洁度",
        "死循环风险"
    ],
    "while 循环": [
        "基于「条件判断」：条件为 True 时持续循环",
        "需要手动定义、初始化和更新（否则易死循环）",
        "1. 循环次数不确定（依赖条件满足与否）；\n2. 需要无限循环（如服务器监听）",
        "次数明确时，代码较繁琐（需手动处理变量）",
        "较高（忘记更新循环变量则无限循环）"
    ],
    "for 循环": [
        "基于「可迭代对象遍历」：遍历完所有元素则循环结束",
        "自动生成循环变量（如 for i in range(5)），无需手动管理",
        "1. 循环次数明确（如遍历 1-10、列表元素）；\n2. 遍历字符串、列表、字典等可迭代对象",
        "次数明确/遍历场景时，代码更简洁高效",
        "极低（除非遍历无限迭代器，如 iter(int,1)）"
    ]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存为 Excel 文件
file_path = r"C:\Users\xin\Desktop\while和for循环对比表.xlsx"
df.to_excel(file_path, index=False, engine="openpyxl")

print(f"Excel 文件已生成：{file_path}")