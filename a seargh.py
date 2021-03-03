vubor = 0
idc = 1
eno = 0
while idc == 1:
    print('   ')
    print('1 = directory')
    print('2 = mnogo')
    print('3 = sort')
    vubor = input(': ')
    if vubor == '1':
        dire = 1
    if vubor == "2":
        mnogo = 1
    if vubor == '3':
        idc = 0
#ypr
mnogo = 0
dire = 0
#-
if dire == 0:
    f = open('/home/student16/Рабочий стол/a_searg')
if dire == 1:
    vubor = input('directoria fqla =:')
    f = open(vubor)
cufra = 0
text = ''
inref = ''
idc = 0
for l in f:
    inref += l
vubor = input('буква: ')
while idc < len(inref):
    if mnogo == 0:
        if 1 > len(vubor):
            vubor = vubor[0]
    if inref[idc] == vubor:
        cufra += 1
        text += vubor
    idc += 1
print(vubor,'=',cufra)
print(text)
vubor = input("ypokovat? = [y]/[n]")