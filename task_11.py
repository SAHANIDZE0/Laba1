vozr=int(input("возраст: "))
dohod=float(input("доход: "))
kredit=float(input("кредит: "))
srok=int(input("срок (мес): "))
ist=input("история (отличная/хорошая/удовл/плохая): ")
por=input("поручители? (да/нет): ")=="да"
zal=input("залог? (да/нет): ")=="да"
otn=kredit/(dohod*srok)
ball=0
if otn<0.3:
    ball+=0
elif otn<0.5:
    ball+=1
elif otn<0.7:
    ball+=2
else:
    ball+=3
if ist=="отличная":
    ball+=0
elif ist=="хорошая":
    ball+=1
elif ist=="удовл":
    ball+=2
else:
    ball+=3
if vozr<25 or vozr>60:
    ball+=1
if por:
    ball-=1
if zal:
    ball-=1
if ball<0:
    ball=0
if ball<=1:
    risk="низкий"
    stavka=12
elif ball<=3:
    risk="средний"
    stavka=16
elif ball<=5:
    risk="высокий"
    stavka=22
else:
    risk="критический"
    stavka=30
print("отношение кредита к доходу:", round(otn, 2))
print("риск:", risk)
print("ставка:", stavka, "%")
