import math

x = math.pi/2

a = math.sin(x**2)
b = math.cos(x**3)
p = (a ** 3) / (b ** 2)

n = math.log(x**2, 3)
d = math.log(x**3, 2)
o = n/d

y = p + o
print(y)