"""import math
fx = []
for x in range(-100,101):
    fx.append(math.sin(x)*100)
print(fx)"""

#értékcsere harmadik változóval
print("értékcsere harmadik változóval")
a = "RS-232"
b = "RS-485"
print(a,b)
c = a
a = b
b = c
print(a,b)
#Egyszerüsített értékcsere, python dolog
print("Egyszerüsített értékcsere")
print(a,b)
a,b = b,a
print(a,b)
