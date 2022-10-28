a = int(input("Birinchi sonni kiriting: "))
b= int(input("Ikkinchi sonni kiriting: "))
amal = input('amallardan birini tanlang: ')

if amal == '+':
    print("Natijangiz:",a+b)
elif amal == '-':
    print("Natijangiz: ",a-b)
elif amal == '*':
    print("Natijangiz: ",a*b)
elif amal == '/':
    print("Natijangiz: ",a/b)
else:
    print("Siz kiritgan amal mavjud emas.")