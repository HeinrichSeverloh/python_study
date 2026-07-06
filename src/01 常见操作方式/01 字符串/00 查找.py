my_str = "hello world and it_cast and it_heima and Python"

# # 1. find()
# print(my_str.find('and'))  # 12
# print(my_str.find('and', 15, 30))  # 23
# print(my_str.find('ands'))  # -1 , ands子串不存在
#
# # 2.index()
# print(my_str.index('and'))  # 12
# print(my_str.index('and', 15, 30))  # 23
# print(my_str.index('ands'))  # 如果index查找子串不存在，报错
#
# # 3.count()
# print(my_str.count('and', 15, 30))
# print(my_str.count('and'))  # 3
# print(my_str.count('ands'))  # 0
#
# # 4.rfind()
# print(my_str.rfind('and'))
# print(my_str.rfind('ands'))
#
# # 5.rindex()
# print(my_str.rindex('and'))
# print(my_str.rindex('ands'))