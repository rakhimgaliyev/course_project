import math


D = 0.071
l = 0.026
d = 0.0

J = math.pi * (D**4 - d**4) / 32

G_delit_c = l / J

print("J:")
print(J)


print("G/c:")
print(G_delit_c)