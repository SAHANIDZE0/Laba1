import random
zag=random.randint(1, 100)
n=0
while True:
    x=int(input("ваше число: "))
    n+=1
    if x<zag:
        print("больше")
    elif x>zag:
        print("меньше")
    else:
        print("угадали с", n, "попытки")
        break
