import math
for x in range(20, 90, 5):
    a = 3* (math.log((x/100)**3)) - 2*(math.log((x/100))**2)

    b = math.e**(2 + 2**(x/100)) + math.e**(3 + 3**(x/100))
    y = a/b
    print(y)
