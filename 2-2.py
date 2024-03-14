a = int(input('Ваш номер:'))
if a in range(0,37) and a % 2 == 0:
    print('Верхнее место')
elif a in range(0,37) and a % 2 != 0:
    print('Нижнее место')

if a in range(36,54) and a % 2 == 0:
    print('Верхнее боковое место')
elif a in range(36, 54) and a % 2 != 0:
    print('Нижнее боковое место')