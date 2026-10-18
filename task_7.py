minut=int(input("минуты: "))
sms=int(input("смс: "))
mb=int(input("мб: "))
itog=24.99
print("базовый тариф: 24.99")
if minut>60:
    c=(minut-60)*0.89
    itog+=c
    print("доп. минуты:", round(c, 2))
if sms>30:
    c=(sms-30)*0.59
    itog+=c
    print("доп. смс:", round(c, 2))
if mb>1024:
    c=(mb-1024)*0.79
    itog+=c
    print("доп. интернет:", round(c, 2))
nalog=itog*0.02
print("налог:", round(nalog, 2))
print("итого:", round(itog+nalog, 2))
