from numpy.random import permutation

str1 ='hello f world'
for i in str1:
    if i == 'f':
        continue

    print(i,end='\t')
print(end='\n')

r"""
 -------------    13
    7  |
4   / 2|2 \       
3  /  3|   \ 
2 /   4|4   \ 
7      |
"""
str2 =r"-------------"
str3 =r"/  |  \ "       #2
str4 =r"/   |   \ "     #3
str5 =r"|"
str6 =r" "
str7 =r"/    |    \ "   #4

a = 12
b = 1

while b > 0:
    print(str6,end='')
    b -= 1
if a == 12:
    print(str2)  #打印第一行
    a += 1

b += 7

while b > 0:
    print(str6,end='')
    b -= 1
if a == 13:
    print(str5)  #打印第一行
    a += 1

b  += 4

while b > 0:
    print(str6,end='')
    b -= 1
if a == 14:
    print(str3)
    a += 1

b += 3

while b > 0:
    print(str6,end='')
    b -= 1
if a == 15:
    print(str4)
    a += 1

b += 2

while b > 0:
    print(str6,end='')
    b -= 1
if a == 16:
    print(str7)
    a += 1

b += 7

while b > 0:
    print(str6,end='')
    b -= 1
if a == 17:
    print(str5)
    a += 1

