# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:06:33 2022
euler.py
"""
from sympy import *
from matplotlib import pyplot as plt
import numpy as np

y=[1.0]
x=[1.0]
x_min=1
x_max=2
N=10
i=0
h=(x_max-x_min)/10
a=Symbol('a',real=True)
b=Symbol('b',real=True)
df=b/(2.0*a)
f=sqrt(a)#解析解

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