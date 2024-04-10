import cmath
z = complex(input())
r = abs(z)
phi = cmath.phase(z)
print(round(r, 3))
print(round(phi, 3))
