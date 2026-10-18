summa=int(input("сумма: "))
for nom in [100, 50, 10, 5, 2, 1]:
    k=summa//nom
    summa=summa%nom
    if k:
        print(nom, "руб -", k, "шт")
