a = input('''Raqamlardan birini tanlang: 
    1==String
    2==Integer
    3==Float
    4==Boolen
    5==List                     ''')

if a =='1':
    print("Siz String ma'lumotni  tanladingiz.")
    b = input('''Quyidagilardan birini tanlang:
    1==O'zingiz haqingizda ma'lumot.
    2==Registratsiyadan o'tish ''')
    if b == '1':
        print("O'zingiz haqingizda ma'lumot kiritishingiz mumkin: ")
        ism = input("Ismingizni kiriting: ")
        familiya = input("Familiyangizni kiriting: ")
    elif b == '2':
        print("Siz registratsiyadan o'tishingiz mumkin:  ")
        email = input("Emailingizni kiriting: ")
        parol = input("Parolni kiriting: ")
        login = input("Loginni kiritting: ")
elif a == '2':
    print("Siz integer ma'lumot tanladingiz.")
    c = input('''Quyidagilardan birini tanlang: 
        1==Kalkulator.
        2==Toq sonlar.
        3==Juft sonlar.
        4== 2 ta nol bilan tugaydigan sonlar yig'indisi.''')
    if c == '1':
        q = int(input("1-son: "))
        w = int(input("2-son: "))
        amal == input("Quyidagilardan amallardan birini tanlang: ")
        if amal == '+':
            print(q+w)
        elif amal == '-':
            print(q-w)
        elif amal == '*':
            print(q*w)
        elif amal == '/':
            print(q/w)
        else:
            print("Siz kiritgan amal mavjud emas.")
    elif c == '2':
        for x in range(1,100,2):
            print(x)

    elif c == '3':
        for x in range(0,100,2):
            print(x)
    elif c == '4':
        a = 0
        b = 100
        while a < b:                        #Xatolik bor.
            a += 100
            b += a
            print(b)




elif a == '3':
    print("Siz float ma'lumot turiga kirdingiz.")
    e = int(input("Qaysi sonning kvadrati kerak:   "))
    print(e**2)
elif a == '4':
    print("Siz boolen ma'lumot turiga kirdingiz.")