x = int(input('введите координату x'))
y = int(input('введите координату y'))
if x > 0 and y > 0:
    print('ваша координата в I четверти')
    print('')
elif x < 0 and y > 0:
    print('ваша координата в II четверти')
    print('')
elif x < 0 and y < 0:
    print('ваша координата в III четверти')
    print('')
elif x > 0 and y < 0:
    print('ваша координата в IV четверти')
else:
    print('вы ввели не корректное значение')
