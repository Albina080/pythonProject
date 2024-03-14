n = int(input('Количество слов:'))
res = ''
for i in range(1, n +1):
    word = str(input('Введите слово:'))
    res = res + ' ' + word
print(res)
