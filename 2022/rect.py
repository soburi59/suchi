# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:46:17 2022

0→1
ans=pi
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
    s+=func.subs(x,xk)*h
print(f"近似値:{float(s)}")