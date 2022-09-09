list = [1, 3, 5, 9, 4, 6, 5, 4, 5, 2, 3]


def number(list):
    result = []
    for i in (list):
        if i not in result:
            result.append(i)
    print(','.join(map(str, result)))


number(list)
