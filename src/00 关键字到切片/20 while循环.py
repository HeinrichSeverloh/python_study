i = 0
while i <= 20:

    if i == 15:
        break

    if i % 2 != 0:
        i += 1
        continue

    print(f"偶数：{i}")
    i += 1

print('\n')

j = 30
while j >= 30:
    if j == 60:
        break

    if j % 2 == 0:
        j += 1
        continue

    print(f'奇数：{j}')
    j += 1