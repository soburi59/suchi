# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 18:51:09 2022
"""
import sympy as sp
k=0
X=[1]
h=2
dX=[]
eps=10**-5
#変数用
x=sp.Symbol('x',real=True)
num=int(input("近似する平方根(整数):"))
original=sp.sqrt(num)
func=(x**2)-(original**2)
print(func.subs(x,X[k])*func.subs(x,X[k]+h))

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
print(f"近似値:{round(X[k],5)}")
