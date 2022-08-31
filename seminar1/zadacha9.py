from calendar import c


a = int(input('введите номер четверти'))
b = "бесконечность"
if a == 1:
    print(f'допустимые значения Xmin=0, Xmax={b}, Ymin=0, Ymax={b}')
elif a == 2:
    print(f'допустимые значения Xmin=0, Xmax=-{b}, Ymin=0, Ymax={b}')
elif a == 3:
    print(f'допустимые значения Xmin=0, Xmax=-{b}, Ymin=0, Ymax=-{b}')
elif a == 4:
    print(f'допустимые значения Xmin=0, Xmax={b}, Ymin=0, Ymax=-{b}')
else:
    print('вы ввели не корректное значение')
