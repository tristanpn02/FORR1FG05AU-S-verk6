def main():
    print('-' * 20)
    print('Veldu forrit:')
    print('\n1) Kennitala\n2) Búa til nýtt orð\n3) Sneið af streng\n0) Hætta')
    try:
        desChoice = int(input('>>> '))

    except :
        print('\nVilla í valmynd! Reyndu aftur')
        main()

    if desChoice == 1:
        lidur1()
    elif desChoice == 2:
        lidur2()
    elif desChoice == 3:
        lidur3()
    elif desChoice == 0:
        exit()

    input('\n[ENTER]')
    main()

def lidur1():
    print('-' * 20)
    desNum = input('\nSláðu inn kennitölu: ')

    while not len(desNum) == 10 or int(str(desNum)[:2]) > 32 or int(str(desNum)[2:4]) > 12 or int(str(desNum)[4:6]) > 18:
        print('Kennitalan vitlaust sláð inn!')
        desNum = input('\nSláðu inn kennitölu: ')
    print('Vel gert þú slóst inn rétta kennitölu', desNum)

def lidur2():
    print('-' * 20)
    word = input('Sláðu inn orð með amk 5 stöfum: ')

    while len(word) < 5:
        print('Orðið er of stutt!')
        word = input('Sláðu inn orð með amk 5 stöfum: ')

    word = word[:2] + word[-2:]

    print('Nýji strengurinn er:', word)
    print('Nýji strengurinn í upphafsstöfum:', word.upper())
    print('Nýji strengurinn í lágstöfum:', word.lower())

def lidur3():
    print('-' * 20)
    word = input('Sláðu inn nafn: ')
    char_list = [x for x in word]

    while len(char_list) > 0:
        print(''.join(char_list))
        char_list.pop(0)
main()
