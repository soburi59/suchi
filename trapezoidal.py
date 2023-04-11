# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 09:20:56 2022

"""

import sympy as sp
n=1000
x=sp.Symbol('x',real=True)
func=4/(1+x*x)

a=0
b=1
h=(b-a)/n
s=0

for k in range(n):
    xk=a+k*h
    xk2=xk+h
    s+=(h*(func.subs(x,xk)+func.subs(x,xk2)))/2
print(f"近似値:{float(s):}")