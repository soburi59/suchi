# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:54:38 2022

"""
import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
k=0
X=[0]
h=5*10**(-4)
dX=[]
eps=10**-10
E=1
R=1095
C=1*(10**-6)
L=0.3
#変数用
x=sp.Symbol('x',real=True)
func=(E/L)*x*sp.E**(-x*R/(2*L))-(E/(R*sp.E))
print(float(func.subs(x,X[k])*func.subs(x,X[k]+h)))

while True:
    h/=2
    if func.subs(x,X[k])*func.subs(x,X[k]+h)<0:
        X.append(X[k])
    else:
        X.append(X[k]+h)
    k+=1
    if eps>h:
        break
print(f"反復回数:{k+1}")
print(f"近似値:{round(X[k],9)}")