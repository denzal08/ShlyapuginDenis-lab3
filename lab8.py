n = int(input("введите количество чисел N:"))
arr = []
for i in range(n):
    value = float(input(f"введите число {i + 1}:"))
    arr.append(value)
index_min = arr.index(min(arr))
index_max = arr.index(max(arr))
left = min(index_min, index_max)
right = max(index_min, index_max)
sum = sum(arr[left + 1:right])
print(f"сумма элементов между мин и макс: {sum}")
