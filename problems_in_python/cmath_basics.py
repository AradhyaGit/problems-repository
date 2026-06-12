import cmath
userinput = input()
comp = complex(userinput)
value = abs(comp)
pha = cmath.phase(comp)

print(value)
print(pha)