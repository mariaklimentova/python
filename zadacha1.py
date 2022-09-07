from re import S


list = [1, 2, 3, 4, 5]
s = 0
for i in list:
    if i % 2 != 0:
        s += i
print(f"сумма не четных чисел = {s}")
