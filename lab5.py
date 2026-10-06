n = int(input("сколько чисел"))
sum3 = 0
sum5 = 0
for i in range(1, n + 1):
    num = float(input("введите" + str(i) + "-e число:"))
    if i % 3 == 0:
        sum3 += num
    elif i % 5 == 0:
        sum5 += num
        print("сумма на позициях, кратных 3:", sum3)
        print("суммф на позициях, кратных 5:(без кратных 3):", sum5)
        print("разность:", sum3 - sum5)