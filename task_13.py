vhod=input("числа через пробел: ").split()
chisla=[]
for x in vhod:
    if "." in x:
        chisla.append(float(x))
    else:
        chisla.append(int(x))
un=[]
for x in chisla:
    if x not in un:
        un.append(x)
print("уникальные:", un)
povt=[]
for x in un:
    if chisla.count(x)>1:
        povt.append(x)
print("повторяющиеся:", povt)
ch=[x for x in chisla if isinstance(x, int) and x%2==0]
nch=[x for x in chisla if isinstance(x, int) and x%2!=0]
print("четные:", ch)
print("нечетные:", nch)
print("отрицательные:", [x for x in chisla if x<0])
print("дробные:", [x for x in chisla if isinstance(x, float)])
print("сумма кратных 5:", sum(x for x in chisla if x%5==0))
mx=chisla[0]
mn=chisla[0]
for x in chisla:
    if x>mx:
        mx=x
    if x<mn:
        mn=x
print("максимум:", mx)
print("минимум:", mn)
