import random
main = 1
bot = random.randint(1,10)
while main == 1:
    qs = int(input("kakaa qifra = "))
    if qs == bot:
        print("horosh")
        main = 0
    else:
        print("lox")
        print("poprobiq eshe raz")
        if qs > bot:
            print("menshe")
        else:
            print("bolshe")