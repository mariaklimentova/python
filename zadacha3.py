import random
b = random.randint(0, 100)
print(b)

k = 2
result = (f'2*{b}^{k}+4*{b}+5=0')
with open('file.txt', 'w') as data:
    data.write(result)
    data.close
