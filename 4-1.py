def delit():
    a = int(input('Введите число: '))
    if a % 3 == 0:
        print('Число делится на 3')
    else:
        print('Число не делится на 3')

def del100():
    b = 0
    try:
        a = input('Введите число: ')
        b = 100 / int(a)
    except ZeroDivisionError:(
        print('Ошибка! а = 0'))
    except ValueError:(
        print('Ошибка! Введите число!'))
    print(b)

def magic():
    a = input('Введите дату: ')
    num = a.split('.')
    print(num)
    day = num[0]
    month = num[1]
    year = num[2]
    b = int(day) * int(month)
    if str(b) in year:
        print('True')
    else:
        print('False')

def lucky():
    a = str(input('Введите счастливый билет: '))
    if len(a) % 2 != 0:
       print('Ошибка! Введено нечетное количество символов')
    else:
        b = list(a)
        c = len(a)
        sum1 = 0
        sum2 = 0
        for i in range(0, int(c / 2)):
            sum1 = sum1 + int(b[i])
        for i in range(int(c / 2), int(c)):
            sum2 = sum2 + int(b[i])
        if sum1 == sum2:
            print('Билет счастливый!')
        else:
            print('Билет не счастливый')