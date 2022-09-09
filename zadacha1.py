a = int(input('введите число'))


def calculation(a):
    result = []
    divider = 2
    while divider <= a:
        if a % divider == 0:
            result.append(divider)
            a = a/divider
        else:
            divider += 1
    print(",".join(map(str, result)))


calculation(a)
