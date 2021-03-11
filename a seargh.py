import random
correct_pass = ''
password = ''
poputok = 0
idc = 0
eno = 0
rand = 0
main = 0
age = 0
age_tier = 0
region = ''
pass_kolvo = 0
region_see = ['russia','america','africa','indonesia','japan','egupt','kazashstan','evropa']
region_pass = [['водка','путин','ячсмитьбюфывапролджэйцукенгшщзхъ'],['zapad','rapqaswdefrgthyjukilop','gniet'],['pesok','N_word','voda'],['indequ','vr','azia'],['anime','naruto','manga'],['svinks','piromida','nil'],['goru','tanci','kymus'],['baget','fashistu','dorogi']]
age_pass = ['ZXCVBNM<>?ASDFDGHJKL:"QWERTYUIIOOP{}|!@#$%^&*()_+12345678890qwertyuiop[]asdfghjkl;','1234567890!@#$%^zxcvbnm,./qwertyuiop[ASDFGHJKL:"','1234567asdfghjklqwezxc']
print('select region:')
while idc < len(region_see):
    print(idc+1,'=',region_see[idc])
    idc += 1
region = int(input('= '))-1
print('enter age:')
age = int(input('= '))
if age < 18:
    age_tier = 0
if age >= 18:
    age_tier = 1
if age >= 40:
    age_tier = 2
print('skolko qufr (minimum 8)')
pass_kolvo = int(input('= '))
if pass_kolvo < 2:
    pass_kolvo = 2
idc = 0
while idc < pass_kolvo:
    rand = random.randint(1,2)
    if rand == 1:
        eno = random.randint(0,2)
        correct_pass += region_pass[region][eno][random.randint(0,len(region_pass[region][eno])-1)]
        eno = 0
        idc += 1
    if rand == 2:
        correct_pass += age_pass[age_tier][random.randint(0,len(age_pass[age_tier])-1)]
        idc += 1
idc = 0
eno = 0
print(correct_pass)
while not password == correct_pass:
    while idc < pass_kolvo:
        rand = random.randint(1,2)
        if rand == 1:
            main = random.randint(0,2)
            password += region_pass[region][main][random.randint(0,len(region_pass[region][eno])-1)]
            main = 0
            idc += 1
        if rand == 2:
            password += age_pass[age_tier][random.randint(0,len(age_pass[age_tier])-1)]
            idc += 1
    if not password == correct_pass:
        eno = 0
        poputok += 1
        idc = 0
        password = ''
print('poputok =',poputok)
print('correct =',password)