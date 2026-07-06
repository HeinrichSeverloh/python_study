import operator

# 定义运算符与对应函数的映射关系（键为运算符字符串，值为运算函数）
operator_map = {
    # 算术运算符
    '+': operator.add,
    '-': operator.sub,
    '✖️': operator.mul,
    '➗': operator.truediv,
    # 比较运算符
    '>': operator.gt,
    '<': operator.lt,
    '==': operator.eq,
    '≠': operator.ne,
    '≥': operator.ge,
    '≤': operator.le
}

# 输入数据
num1 = float(input("请输入第一个数字："))
op = input("请输入运算符（支持 + - ✖️ ➗ > < == ≠ ≥ ≤）：")
num2 = float(input("请输入第二个数字："))

# 检查运算符是否支持
if op not in operator_map:
    print(f"不支持的运算符：{op}")
else:
    # 执行运算
    try:
        result = operator_map[op](num1, num2)
        # 输出结果（区分算术运算和比较运算的显示方式）
        if op in ['+', '-', '✖️', '➗']:
            print(f"{num1} {op} {num2} = {result}")
        else:
            print(f"{num1} {op} {num2} 的结果是：{result}（True表示成立，False表示不成立）")
    except ZeroDivisionError:
        print("错误：除数不能为0")
