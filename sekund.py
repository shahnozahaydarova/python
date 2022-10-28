import time
kod = int(input("Kodni kiriting:  "))

if kod == 12345:
    print("Tizimga kirishingiz mumkin.")
elif kod !=12345:
    print("kod xato kiritilgan va kuting")
    
    a = 0
    b = 60
    while a<b:
        time.sleep(0.5)
        a+=1
        print(a)
  
