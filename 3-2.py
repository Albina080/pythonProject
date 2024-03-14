res = ''
while True:
    word = str(input('Введите слово:'))
    if 'stop' in word:
        break
    res = res + ' ' + word
print(res)

