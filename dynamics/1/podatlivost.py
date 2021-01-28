import math


D = 0.100
l = 0.200
d = 0.040

J = math.pi * (D**4 - d**4) / 32

G_delit_c = l / J

print("J:")
print(J)


print("G/c:")
print(G_delit_c)