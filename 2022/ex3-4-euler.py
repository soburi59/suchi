# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:33:38 2022
ex3-4-euler.py
"""
from sympy import *
from matplotlib import pyplot as plt
import numpy as np

y=[1.0]
x=[1.0]
x_min=1
x_max=20
i=0
h=0.5
a=Symbol('a',real=True)
b=Symbol('b',real=True)
df=(b*2)/a
f=a*a#解析解

while x[i]<x_max:
    temp=float(y[i]+h*df.subs([(a,x[i]),(b,y[i])]))
    y.append(temp)
    x.append(round(x[i]+h,1))
    i+=1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y,label="approximate solution")
ax.plot(x,[f.subs(a,i) for i in x],label="analytical solution")
ax.legend()