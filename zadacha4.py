a = int(input('введите число'))
resalt = []
while a >= 1:
    if a < 1:
        break
    if a % 2 == 0:
        a = a/2
        resalt.insert(0, 0)
    if a / 2 != 0:
        a = a//2
        resalt.insert(0, 1)
print(resalt)
