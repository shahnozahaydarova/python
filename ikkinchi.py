class Kasb:
    def __init__(self,maosh,tajriba):
        self.maosh = maosh
        self.tajriba = tajriba
    def __str__(self):
        return f"Maoshi: {self.maoshi} Tajriba: {self.tajriba}"



class Tikuvchi(Kasb):
    def __init__(self,maosh,tajriba,jihozlari):
        super(). __init__(maosh,tajriba)
        self.jihozlari = jihozlari
    def chiqarish(self):
        print("Maoshi: ",self.maosh,"Tajribasi: " self.tajriba,"Jihozlari: ", self.jihozlari)

t1 = Tikuvchi("100000","2yil","tikuv mashinka")
t2 = Tikuvchi("150000","3yil","tikuv mashinka")
t3 = Tikuvchi("200000","5yil","tikuv mashinka")
print(t1)
print(t2)
print(t3)

