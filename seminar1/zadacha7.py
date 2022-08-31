x = [True, False]
y = [True, False]
z = [True, False]
for i in x:
    for f in y:
        for d in z:
            print(f'{not (x or y  or z) == (not x and not y and not z)}')