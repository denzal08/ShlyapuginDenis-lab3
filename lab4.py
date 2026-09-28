import math

total = 0
for n in range(1, 51):
    trem = ((-1) ** n) * (n + 2) / math.factorial(2 * n + 1) * math.cos(n)
    total += trem
    print(total)