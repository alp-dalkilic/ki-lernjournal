def Uebung_1():# Temparatur-Klassifikator
    temperatur = 0
    print('Geben sie ihre gefühlte Temperatur ein:')
    temperatur = float(input('>'))
    if temperatur < 10:
        print('kalt')
    elif temperatur >=10 and temperatur <=25:
        print('mild')
    else:
        print('heiß')

def Uebung_2():# Typumwandlung
    Zahl1 = input('>>')
    Zahl2 = input('>>')
    Zahl3 = int(Zahl1) + int(Zahl2)
    print('Summe = ' + str(Zahl3))

def Uebung_3(): #Gerade/Ungerade
    Zahl = input('>>')
    if float(Zahl) % 2 == 0:
        print('Gerade')
    else:
        print('Ungerade')


Uebung_3()
