a = int(input("Birinchi sonni kiriting: "))
amal1 = input("Birinchi amalni kiriting: ")
b = int(input("ikkinchi sonni kiriting: "))
amal2 = input("Ikkinchi amalni kiriting: ")
c = int(input("Uchinchi sonni kiriting: "))

if amal1 == '+' and amal2 == '+':
    print("Natijangiz: ",a+b+c)
elif amal1 == '+' and amal2 == '-':
    print("Natijangiz: ",a+b-c)
elif amal1 == '+' and amal2 == '*':
    print("Natijangiz: ",(a+b)*c)
elif amal1 == '+' and amal2 == '/':
    print("Natijangiz: ",a+b/c)
elif amal1 == '-' and amal2 == '+':
    print("Natijangiz: ", a-b+c)
elif amal1 == '-' and amal2 == '-':
    print("Natijangiz: ",a-b-c)
elif amal1 == '-' and amal2 == '*':
    print("Natijangiz: ",(a-b)*c)
elif amal1 == '-' and amal2 == '/':
    print("Natijangiz: ",(a-b)/c)
elif amal1 == '*' and amal2 == '+':
    print("Natijangiz: ", a*b+c)
elif amal1 == '*' and amal2 == '-':
    print("Natijangiz: ",a*b-c)
elif amal1 == '*' and amal2 == '*':
    print("Natijangiz: ",a*b*c)
elif amal1 == '*' and amal2 == '/':
    print("Natijangiz: ",a*b/c)
elif amal1 == '/' and amal2 == '+':
    print("Natijangiz: ", a/b+c)
elif amal1 == '/' and amal2 == '-':
    print("Natijangiz: ",a/b-c)
elif amal1 == '/' and amal2 == '*':
    print("Natijangiz: ",a/b*c)
elif amal1 == '/' and amal2 == '/':
    print("Natijangiz: ",a/b/c)
else:
    print("Siz kiritgan amal tizimda mavjud emas.")

