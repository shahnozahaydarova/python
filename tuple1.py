moshin = {
    "chevrolet":{
        "f1":['Nexia','12000$'],
        "f2":['Leganza','13000$'],
        "f3":["Statesman",'150000$'],
    },
    "hyundai":{
        "h1":['Creta','150000$'],
        "h2":['Tucson','343400$'],
        "h3":['Elantra','34535$'],
    },
    "isuzu":{
        "i1":["Pick up","1224$"],
        "i2":["Belleti","120009$"],
        "i3":["Unicab",'120000$']
    }
}
avtomobil = input('''Sizga qaysi turdagi avtomobil kerak:   chevrolet       hyundai         isuzu
                        ''')
if avtomobil.lower() ==  'chevrolet':
    a = input('''Siz chevrolet avtomobiliga tegishli brendlardan quyidagilarni xarid qilishingiz mumkin:     nexia      leganza     statesman
                 ''')
    if a.lower() == 'nexia':
        print("Siz",moshin["chevrolet"]["f1"][0],"avtomobilini",moshin["chevrolet"]["f1"][1],"so'mga xarid qilishingiz mumkin.")
    elif a.lower() == 'leganza':
        print("Siz",moshin["chevrolet"]["f2"][0],"avtomobilini",moshin["chevrolet"]["f2"][1],"so'mga xarid qilishingiz mumkin.")
    elif a.lower() == 'statesman':
        print("Siz",moshin["chevrolet"]["f3"][0],"avtomobilini",moshin["chevrolet"]["f3"][1],"so'mga xarid qilishingiz mumkin.")

if avtomobil.lower() ==  'hyundai':
    a = input('''Siz hyundai avtomobiliga tegishli brendlardan quyidagilarni xarid qilishingiz mumkin:     creta      tucson     elantra
                 ''')
    if a.lower() == 'creta':
        print("Siz",moshin["hyundai"]["h1"][0],"avtomobilini",moshin["hyundai"]["h1"][1],"so'mga xarid qilishingiz mumkin.")
    elif a.lower() == 'tucson':
        print("Siz",moshin["hyundai"]["h2"][0],"avtomobilini",moshin["hyundai"]["h2"][1],"so'mga xarid qilishingiz mumkin.")
    elif a.lower() == 'elantra':
       print("Siz",moshin["hyundai"]["h3"][0],"avtomobilini",moshin["hyundai"]["h3"][1],"so'mga xarid qilishingiz mumkin.")

if avtomobil.lower() ==  'isuzu':
    a = input('''Siz hyundai avtomobiliga tegishli brendlardan quyidagilarni xarid qilishingiz mumkin:     creta      tucson     elantra
                 ''')
    if a.lower() == 'creta':
        print("Siz",moshin["isuzu"]["i1"][0],"avtomobilini",moshin["isuzu"]["i1"][1],"so'mga xarid qilishingiz mumkin.")
    elif a.lower() == 'tucson':
        print("Siz",moshin["isuzu"]["i2"][0],"avtomobilini",moshin["isuzu"]["i2"][1],"so'mga xarid qilishingiz mumkin.")
    elif a.lower() == 'elantra':
       print("Siz",moshin["isuzu"]["i3"][0],"avtomobilini",moshin["isuzu"]["i3"][1],"so'mga xarid qilishingiz mumkin.")
