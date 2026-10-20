stroka = input("введите числа через пробел:").split()
numbers = []
for s in stroka:
    n = float(s)
    if n > 0:
        numbers.append(n * n)
print(numbers)