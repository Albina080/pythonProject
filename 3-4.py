import random

r = 0
w = 0
while w < 3:
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = int(input(str(a) + '+' + str(b) + '='))
    if a + b == c:
        r += 1
        print("Правильно!")
    else:
        w += 1
        print('Ответ неверный')
        if w == 3:
            print('Игра окончена. Правильных ответов: ' + str(r))