from fractions import Fraction
import numpy as np
n = Fraction(eval(input("Enter power of the x:"))).limit_denominator(10)
c = Fraction(eval(input("Enter co-efficient of x:"))).limit_denominator(10)
der = f"{c*n}(x**{n-1})"
print(f"Derivation(d/dx):{der}")
point1 = float(input("Enter point(a):"))
point2 = float(input("Enter point(b):"))
a = (c*n)*((point1)**(n-1))
b = (c*n)*((point2)**(n-1))
print(f"Integral of f(x) = {c}x**{n} :{np.abs(b-a)}")
