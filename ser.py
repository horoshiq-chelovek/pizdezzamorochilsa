import random

vubor = 0
idc = 0
menu = 1
#mas = [50,25,10,5,1]
mas = [0,0,0,0,0]

kop = int(input('skolko qentov = '))
while menu == 1:
    if kop >= 50:
        kop -= 50
        mas[0] += 1
    else:
        if kop >= 25:
            kop -= 25
            mas[1] += 1
        else:
            if kop >= 10:
                kop -= 10
                mas[2] += 1
            else:
                if kop >= 5:
                    kop -= 5
                    mas[3] += 1
                else:
                    if kop >= 1:
                        kop -= 1
                        mas[4] += 1
    if kop <= 0:
        menu = 0
print('50 центов =',mas[0])
print('25 центов =',mas[1])
print('10 центов =',mas[2])
print('5  центов =',mas[3])
print('1  цент   =',mas[4])