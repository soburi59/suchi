# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:20:23 2022
ex3-4
"""

import sympy as sp
from matplotlib import pyplot as plt
import numpy as np

y=[1.0]
x=[1.0]
x_min=1
x_max=20
i=0
h=0.5
a=sp.Symbol('a',real=True)
b=sp.Symbol('b',real=True)
df=(2*b)/a
f=a*a

dim=input("n次:")
while x[i]<x_max:
    k1=float(h*df.subs([ (a,x[i]) , (b,y[i]) ]))
    k2=float(h*df.subs([ (a,x[i]+h/2) , (b,y[i]+k1/2) ]))

    if dim=="2":
        y.append(float( y[i]+k2 ))
    elif dim=="3":
        k3=float(h*df.subs([ (a,x[i]+h) , (b,y[i]+2*k2-k1) ]))
        y.append(float( y[i]+(k1+ 4*k2+k3)/6 ))
    elif dim=="4":
        k3=float(h*df.subs([ (a,x[i]+h/2) , (b,y[i]+k2/2) ]))
        k4=float(h*df.subs([ (a,x[i]+h) , (b,y[i]+k3) ]))
        y.append(float( y[i]+(k1+2*k2+ 2*k3+k4)/6) )
    x.append(round( x[i]+h,1 ))
    i+=1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y,label="y")
ax.plot(x,[f.subs(a,i) for i in x],label="original")
ax.legend()