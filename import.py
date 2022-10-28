try:
    from form import *
    import time
    print(login)
    print(parol)
    if login == 1234 and parol == 5678:
        print("Tizimga kirishingiz mumkin.")
    elif login != 1234 and parol == 5678:
        print("Login noto'g'ri kiritilgan.")
        a = 0
        while a<10:
            a+=1
            time.sleep(1)
            print(a)
    elif login == 1234 and parol != 5678:
        print("Parol noto'g'ri kiritilgan.")
        a = 0
        while a<10:
            a+=1
            time.sleep(1)
            print(a)
    elif login != 1234 and parol != 5678:
        print("Login va parol  noto'g'ri kiritilgan.")
        a = 0
        while a<60:
            a += 1
            time.sleep(1)
            print(a)
except:
    print("Siz string qiymat kiritdingiz.")