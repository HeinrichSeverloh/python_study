set1 = {1,2,3,4}
print('原集合:',set1)

# 1.remove函数  有则删除,无则报错
# 集合名.remove(元素)
# 第一种: 有
set1.remove(3)
print(set1)  # {1, 2, 4}
# 第二种: 无
# set1.remove(5)   *报错*

# 2.pop函数  默认删除hash表排序后的左边的第一个元素
set2 = {1,2,3,4}
print('原集合',set2)
# (1) 数字
set2.pop()
print(set2)  #

set3 = {'a','b','c','d'}
print('原集合',set3)
set3.pop()
print(set3)  #每次删除的都是左边第一个元素,每次都不一样
