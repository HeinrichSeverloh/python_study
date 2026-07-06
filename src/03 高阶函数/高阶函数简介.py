# 4.1 体验高阶函数

# 高阶函数是指可以接受函数作为参数，或者返回函数的函数

# 1.1内置函数
# abs() 是一个内置函数，用于获取数字的绝对值
print(abs(-5))  # 输出: 5
print(abs(5))   # 输出: 5

# round() 是一个内置函数，用于对数字进行四舍五入
print(round(3.14159))  # 输出: 3
print(round(3.5))      # 输出: 4

# 1.2 自定义高阶函数

# 方法1 
def add_num1(a, b):
    return abs(a) + abs(b)

result = add_num1(-3, 5)
print(result)  # 输出: 8

# 方法2

def sum_num2(a, b, f):
    return f(a) + f(b)

result = sum_num2(-3, 5, abs)
print(result)  # 输出: 8

# 注意： 两种方法对比之后，发现，方法2更加代码简洁，函数灵活性更高
# 函数式编程大量使用函数，减少代码重复，提高代码的可读性和可维护性