units={
    "длина": {"мм": 0.001, "см": 0.01, "м": 1, "км": 1000, "дюйм": 0.0254, "фут": 0.3048},
    "масса": {"мг": 0.000001, "г": 0.001, "кг": 1, "т": 1000, "фунт": 0.4536},
    "время": {"сек": 1, "мин": 60, "час": 3600, "сутки": 86400},
    "температура": {"C": 1, "F": 1, "K": 1}
}
print("типы:", list(units.keys()))
t=input("тип: ")
print("единицы:", list(units[t].keys()))
otkuda=input("из: ")
kuda=input("в: ")
znach=float(input("значение: "))
if t=="температура":
    if otkuda=="C":
        c=znach
    elif otkuda=="F":
        c=(znach-32)*5/9
    else:
        c=znach-273.15
    if kuda=="C":
        r=c
    elif kuda=="F":
        r=c*9/5+32
    else:
        r=c+273.15
else:
    r=znach*units[t][otkuda]/units[t][kuda]
print("результат:", round(r, 4), kuda)
