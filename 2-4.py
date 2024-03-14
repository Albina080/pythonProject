a = str(input('Введите первый основной цвет:'))
b = str(input('Введите второй основной цвет:'))
k = 'красный'
s = 'синий'
j = 'желтый'

if k in a or s in a or j in a and k in b or s in b or j in b:
    if k in a and k in b or s in a and s in b or j in a and j in b:
        b = str(input('Введите другой основной цвет: '))
        if k in a and s in b:
            print('Вторичный цвет - фиолетовый')
        elif k in a and j in b:
            print('Вторичный цвет - оранжевый')
        elif s in a and k in b:
            print('Вторичный цвет - фиолетовый')
        elif s in a and j in b:
            print('Вторичный цвет - зеленый')
        elif j in a and k in b:
            print('Вторичный цвет - оранжевый')
        elif j in a and s in b:
            print('Вторичный цвет - зеленый')
    else:
        if k in a and s in b:
            print('Вторичный цвет - фиолетовый')
        elif k in a and j in b:
            print('Вторичный цвет - оранжевый')
        elif s in a and k in b:
            print('Вторичный цвет - фиолетовый')
        elif s in a and j in b:
            print('Вторичный цвет - зеленый')
        elif j in a and k in b:
            print('Вторичный цвет - оранжевый')
        elif j in a and s in b:
            print('Вторичный цвет - зеленый')
else:
    print('Ошибка!')