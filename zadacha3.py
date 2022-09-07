list = [5, 4, 1.5, 3.8]
b = 0
c = 0
for i in list:
    if i > b:
        b = i
        c = b
        for s in list:
            if s > 0 and s < c:
                c = s
print(b - c)
