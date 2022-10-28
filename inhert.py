class Hayvon:
    def __init__(self,yosh,rang):
        self.yosh = yosh
        self.rang =rang
    
    def chiqarish1(self):
        print("Yoshi: ", self.yosh, "Rangi: ", self.rang)

h1 = Hayvon(1,"qora")
h2 = Hayvon(2,"oq")

print(h1.chiqarish1())
print(h2.chiqarish1())


class  Mushuk(Hayvon):
    def __init__(self,yosh,rang,tur):
        super().__init__(yosh,rang)
    def chiqarish2(self):
        print("Yoshi: ", self.yosh,"Rangi: ",self.rang,"Turi: " ,self.tur)

m1 = Mushuk