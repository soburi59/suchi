# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:34:56 2022
"""

import sympy as sp
n=1000
x=sp.Symbol('x',real=True)
func=4/(1+x*x)

a=0
b=1
h=(b-a)/n
s=0

for k in range(int(n/2)):
    xk=a+2*k*h
    xk2=xk+h
    xk3=xk2+h
    s+=(h*(func.subs(x,xk)+4*func.subs(x,xk2)+func.subs(x,xk3)))/3
print(f"近似値:{float(s)}")