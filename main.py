def main():
    print('-' * 20)
    #Prenta út valmynd
    print('Veldu forrit:')
    print('\n1) Kennitala\n2) Búa til nýtt orð\n3) Sneið af streng\n0) Hætta')
    # Prófa að fá val notanda
    try:
        desChoice = int(input('>>> '))

    # Ef villa kom upp, prentar valmynd aftur
    except :
        print('\nVilla í valmynd! Reyndu aftur')
        main()

    # Keyra forrit eftir vali
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
    # Fá kennitölu
    desNum = input('\nSláðu inn kennitölu: ')

    # Athuga hvort að rétt var sláð inn
    while not len(desNum) == 10 or int(str(desNum)[:2]) > 32 or int(str(desNum)[2:4]) > 12 or int(str(desNum)[4:6]) > 18:
        print('Kennitalan vitlaust sláð inn!')
        desNum = input('\nSláðu inn kennitölu: ')

    # Prenta að rétt var sláð inn + kennitölu
    print('Vel gert þú slóst inn rétta kennitölu', desNum)

def lidur2():
    print('-' * 20)
    # Fá orð
    word = input('Sláðu inn orð með amk 5 stöfum: ')

    # Athuga hvort að orðið sé örugglega 5 stafir eða meira
    while len(word) <= 5:
        print('Orðið er of stutt!')
        word = input('Sláðu inn orð með amk 5 stöfum: ')

    # Búa til nýtt orð með fyrstu 2 og síðustu 2 stöfum
    word = word[:2] + word[-2:]

    # Prenta nýja orðið
    print('Nýji strengurinn er:', word)
    print('Nýji strengurinn í upphafsstöfum:', word.upper())
    print('Nýji strengurinn í lágstöfum:', word.lower())

def lidur3():
    print('-' * 20)
    # Fá nafn
    word = input('Sláðu inn nafn: ')
    # Setja stafi í lista
    char_list = [x for x in word]

    # Á meðan að listinn er meira en 1 stafur
    while len(char_list) > 0:
        # Tengja stafina saman og prenta
        print(''.join(char_list))
        # Fjarlægja 1. staf frá lista
        char_list.pop(0)

# Keyra forritið        
main()
