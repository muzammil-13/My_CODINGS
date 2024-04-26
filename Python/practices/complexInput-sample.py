import cmath

a=2+3j

print(f"Result= {a}")

r1,phi1=cmath.polar(a)

print(f"a in polar coordinates is = ({r1},{phi1})")

z8=cmath.rect(r1,phi1)

print(f"(r1,phi1) in complex form is z8= {z8}")