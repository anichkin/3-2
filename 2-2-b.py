def top10(text, coding):
    all_news = []
    with open(text, encoding=coding) as f:
        all_news.append(f.read().strip('\n'))
        words = all_news[0].split()
        words.sort()
        words_repeat = {}
        repeat = 0
        for i in range(0, len(words) - 1):
            if words[i] == words[i + 1] and len(words[i]) > 6:
                repeat += 1
            else:
                words_repeat[words[i]] = repeat
                repeat = 0

    def max_pair():
        for key, repeat in words_repeat.items():
            if repeat == max(words_repeat.values()):
                print(key, repeat)
                words_repeat.pop(key)
                break

    for i in range(10):
        max_pair()


def program():
    all_news = []
    print('введите команду: ')
    print('1 - вывод по всем файлам')
    print('2 - ручной ввод')
    command = input('введите команду: ')
    if command == '1':
        print('файл newsafr.txt')
        top10('newsafr.txt', 'UTF-8')
        print()
        print('файл newscy.txt')
        top10('newscy.txt', 'KOI8-R')
        print()
        print('файл newsfr.txt')
        top10('newsfr.txt', 'ISO-8859-5')
        print()
        print('файл newsit.txt')
        top10('newsit.txt', 'CP1251')
        print()
        program()
    elif command == '2':
        text = input('Введите название текста с расширением ')
        coding = input('Введите кодировку файла ')
        top10(text, coding)
        program()


program()
