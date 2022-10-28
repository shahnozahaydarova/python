karta = input("karta raqamini kiriting: ")
raqam = input("telefon raqamingizni kiriting")

if karta == "0331" and raqam == "9999":
    print("siz tizimga kirdingiz: ") 
elif karta != "0331" and raqam == "9999":
    print("kartani to'g'ri kiriting")
elif karta == "0331" and raqam != "9999":
    print("raqamni to'g'ri kiriting: ")
else:
    print("siz tizimga kira olmaysiz. ")
    



