while True:
    word = str(input('Ведите слово:'))
    proverka = list(word)
    if 'ф' in proverka:
        print("Ого! Это редкое слово!")
        break
    else:
        print("Эх, это не очень редкое слово...")
        break
