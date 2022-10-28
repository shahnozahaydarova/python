ism = input("ismingizni kiriting:")
familiya = input("familiyangizni kiriting: ")
parol = input("parolni kiriting")
if ism=="shukrona" and familiya=="nurova" and parol=="0331":
    print("siz tizimga kirdingiz")
elif ism!="shukrona" and familiya=="nurova" and parol=="0331":
    print("ism noto'g'ri")
elif ism!="shukrona" and familiya!="nurova" and parol=="0331":
    print("ism va familiya noto'g'ri")
elif ism!="shukrona" and familiya=="nurova" and parol!="0331":
    print("ism va parol noto'g'ri")
elif ism=="shukrona" and familiya!="nurova" and parol!="0331":
    print("familiya va parol noto'g'ri")
else:
    print("siz tizimga kira olmadingiz")

