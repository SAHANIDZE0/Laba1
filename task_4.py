a=float(input("a = "))
b=float(input("b = "))
print("сумма:", a+b)
print("разность:", a-b)
print("произведение:", a*b)
if b!=0:
    print("частное:", a/b)
    print("остаток:", a%b)
else:
    print("на ноль делить нельзя")
try:
    print("степень:", a**b)
except:
    print("степень посчитать не удалось")
