vubor = 0
idc = 1
eno = 0
dire = 1
cufra = 0
text = ''
inref = ''
while idc == 1:
    print('   ')
    print('1 = directory',dire)
    print('2 = start')
    vubor = input(': ')
    if vubor == '1':
        dire = 1
    if vubor == '2':
        idc = 0
if dire == 1:
    vubor = input('расположение файла =:')
    f = open(vubor)
for l in f:
    inref += l
vubor = input('буква: ')
idc = 0
while idc < len(inref):
    if inref[idc] == vubor:
        cufra += 1
        text += vubor
    idc += 1
print(vubor,'=',cufra)
print(text)