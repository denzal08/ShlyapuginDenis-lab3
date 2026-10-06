import math
n = int(input("сколько чисел?"))
count = 0
total = 0
for i in range(1, n + 1):
    num = int(input("введите" + str(i) + "-e число:"))
    root = int(math.isqrt(num))
    if root * root == num:
        count += 1
        total += num
        print("количество полных квадратов:", count)
        print("сумма полных квадратов:", total)