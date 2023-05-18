# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:06:33 2022
"""
import sympy as sp
from matplotlib import pyplot as plt
import numpy as np
import math

y=[1.0]
x=[0]
temp_z=1
x_min=0
x_max=5
N=10
i=0
h=0.4
a=sp.Symbol('a',real=True)
b=sp.Symbol('b',real=True)
c=sp.Symbol('c',real=True)
ddf=(sp.exp(a))-b-c
f=(2/3)*sp.exp(-a/2)*(sp.cos(sp.sqrt(3)*a/2)+sp.sqrt(3)*sp.sin(sp.sqrt(3)*a/2))+sp.exp(a)/3 #解析解

while x[i]<x_max:
    y.append(y[i]+h*temp_z)
    temp_z=float(temp_z+h*ddf.subs([(a,x[i]),(b,y[i]),(c,temp_z)]))
    x.append(round(x[i]+h,1))
    i+=1

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
ax.plot(x,y,label="euler")
y_=[f.subs(a,i) for i in x]
ax.plot(x,y_,label="answer")
gosalist=[abs(i-j) for i,j in zip(y,y_)]
ax2 = fig.add_subplot(2,1,2)
ax2.plot(x,gosalist,label="measurement error")
ax2.legend()
ax.legend()