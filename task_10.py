summa=float(input("сумма покупки: "))
vozr=int(input("возраст: "))
vip=input("vip? (да/нет): ")=="да"
dr=input("день рождения? (да/нет): ")=="да"
skidka=0
if summa>1000:
    skidka=10
if vozr>=63:
    skidka+=5
if dr:
    skidka+=5
if vip and skidka<15:
    skidka=15
if skidka>25:
    skidka=25
print("скидка:", skidka, "%")
print("к оплате:", round(summa*(1-skidka/100), 2))
