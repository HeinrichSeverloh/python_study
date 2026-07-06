# 赋值(数据全共享)
li1 = [1,2,3,4]

li2 = li1
print('原列表:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
li1.append(5)
print('添加后:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
# 完全共享资源,一改全改
print('li1内存地址:',id(li1))
print('li2内存地址:',id(li2))
# 内存地址相同

# 浅拷贝(数据半共享)
import copy

li1 = [1,2,3,4,[5,6,7]]
li2 = copy.copy(li1)
print('li1内存地址:',id(li1))
print('li2内存地址:',id(li2))
# 内存地址不同,不是同一个对象
print('原列表:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
li1.append(9)
print('添加后:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
li1[4].append(8)
print('添加后:','\n','li1:','\n',li1,'\n','li2:','\n',li2)

# 深拷贝(数据不共享)
li1 = [1,2,3,4,[5,6,7]]
li2 = copy.deepcopy(li1)
print('li1内存地址:',id(li1))
print('li2内存地址:',id(li2))
# 内存地址不同,不是同一个对象
print('原列表:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
li1.append(9)
print('添加后:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
li1[4].append(8)
print('添加后:','\n','li1:','\n',li1,'\n','li2:','\n',li2)
# 两个直接没有任何关联