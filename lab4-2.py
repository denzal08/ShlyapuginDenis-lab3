a=1
for n in range(1,31):
    numenator = n**2 + n + 1
    denominator = n**2 + 2*n**(-2*n) + 6
    a *= numenator / denominator
print(a)