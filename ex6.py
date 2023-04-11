# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 16:05:27 2022

"""

import sympy as sp
n=800 #m=n
x=sp.Symbol('x',real=True)
y=sp.Symbol('y',real=True)
func=x*x*y*y

a=10
b=20
h1=a/n
h2=b/n
v=0


for i in range(n):
    xk=i*h1
    for j in range(n):
        yk=j*h2
        v+=func.subs([(x,xk), (y,yk)])*h1*h2
print(f"近似値:{float(v)}")