class Odam:
    def __init__(self,ism,yosh,vazn):
        self.ism = ism
        self.yosh = yosh
        self.vazn = vazn
    def __str__(self):
        return f"Ismi: {self.ism},Yoshi: {self.yosh}, Vazni: {self.vazn}"

class Talaba(Odam):
    def __init__(self,ism,yosh,vazn,oqishjoyi):
        super(). __init__(ism,yosh,vazn)
        self.oqishjoyi = oqishjoyi
    def chiqarish(self):
        print("Ismingiz:", self.ism, "Yoshingiz:", self.yosh, "Vazni: " ,self.vazn ,"O'qish joyingiz: " ,self.oqishjoyi)

t1 = Talaba("Guli",19,45,"ped institut")
t2 = Talaba("Shaxi",19,40,"gorni institut")
t3 = Talaba("Nozi",19,50,"ped institut")
print(t1.chiqarish())
print(t2.chiqarish())
print(t3.chiqarish())



class Abiturient(Odam):
    def __init__(self,ism,yosh,vazn,tayyorlanganjoyi):
        super().__init__(ism,yosh,vazn)
        self.tayyorlanganjoyi = tayyorlanganjoyi
    def chiqar(self):
        print("Ismingiz: ",self.ism ,"Yoshingiz: " ,self.yosh,"Vazn: ", self.vazn,"Tayyorlangan o'quv markazingiz",self.tayyorlanganjoyi)

a1 = Abiturient("Marjon",16,45,"Nur education")
a2 = Abiturient("Zarin",17,50,"Eldorado")
a3 = Abiturient("Sevinch",15,45,"Madina")

print(a1.chiqar())
print(a2.chiqar())
print(a3.chiqar())

class Ishchi(Odam):
    def __init__(self,ism,yosh,vazn,ishjoyi):
        super().__init__(ism,yosh,vazn)
        self.ishjoyi = ishjoyi
    def retur(self):
        print("Ismingiz: ", self.ism ,"Yoshingiz: ",self.yosh, "Vazn: ",self.vazn,"Ish joyi: ", self.ishjoyi)


i1 = Ishchi("Ma'mur",34,70,"maktab")
i2 = Ishchi("Madina",27,55,"bog'cha")
i3 = Ishchi("Maxliyo",30,60,"o'quv markaz")
print(i1.retur())
print(i2.retur())
print(i3.retur())
