def sum(a,b) :
    """求和函数"""
    a = int(a)
    b = int(b)
    print(a + b)
    return

def reduce(a,b) :
    """求差函数"""
    a = int(a)
    b = int(b)
    print(a - b)
    return

def multiply(a,b) :
    """求积函数"""
    a = int(a)
    b = int(b)
    print(a * b)
    return

def division(a,b) :
    """求商函数"""
    a = int(a)
    b = int(b)
    print(a / b)
    return

while True :
    print('请输入用中间用空格链接的计算式(按q退出): ')
    expression = str(input())
    if len(expression) != 1:
        Slice_data = expression.split()

        if len(Slice_data[1]) == 1 :

            if Slice_data[1] == '+':
                sum(Slice_data[0],Slice_data[2])

            elif Slice_data[1] == '-':
                reduce(Slice_data[0],Slice_data[2])

            elif Slice_data[1] == '*':
                multiply(Slice_data[0],Slice_data[2])

            else: division(Slice_data[0],Slice_data[2])

        else: print('错误!!! 请输入单个计算符!!!')
    else:
        if expression == 'q' :

            break