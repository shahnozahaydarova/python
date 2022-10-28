dikt = {
    "apple":{
        "a1":["13 Pro Max","1250$"],
        "a2":["Mackbook Pro 2022 M2","1800$"],
        "a3":["Iphone 14 Pro","1500$"]
        },
    "Huawei":{
        "h1":["Huawei Nova 9 8/128GB","6000$"],
        "h2":["Huawei Nova 9 SE 8/128 GB Moviy","7000$"],
        "h3":["Huawei Nova Y70 4/128 GB Kristalli ko‘k","8000%"]
    }
}
qiymat = input("Sizga qaysi brend kerak:          apple     huawei ")


if qiymat.lower() == 'apple': 
    # print(dikt["apple"])
    a = input("Sizga apple brendining qaysi mahsuloti kerak:            13 pro         mackbook           14 pro ")
    if a.lower() == '13 pro':
        print(dikt["apple"]["a1"])
    elif a.lower() == 'mackbook':
        print(dikt["apple"]['a2'])
    elif a.lower() == '14 pro':
        print(dikt["apple"]['a3'])

elif qiymat.lower() == 'huawei':
    v = input("Sizga huawei brendining qaysi mahsuloti kerak:           Nova 9 8            Nova 9 SE       Nova y70")
    if a.lower() == 'Nova 9 8':
           print(dikt["Huawei"]["h1"])
    elif v.lower() == 'Nova 9 SE':
        print(dikt[" Huawei"]["h2"])
    elif v.lower() == 'Nova y70':
        print(dikt["apple"]['h3'])
 

