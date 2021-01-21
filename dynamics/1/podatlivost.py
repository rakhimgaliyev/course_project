import math


l = 0.024
D = 0.092
d = 0.030

J = math.pi * (D**4 - d**4) / 32

G_delit_c = l / J

print("J:")
print(J)


print("G/c:")
print(G_delit_c)