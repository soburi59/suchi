   # -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:00:48 2022
"""
import sympy as sp
from matplotlib import pyplot as plt
import numpy as np

y=[1.0]
x=[0.0]
x_min=0
x_max=2.5
N=10
i=0
h=0.1
a=sp.Symbol('a',real=True)
b=sp.Symbol('b',real=True)
df=a*b
f=sp.E**(a**2/2)#解析解

while x[i]<x_max:
    temp=float(y[i]+h*df.subs([(a,x[i]),(b,y[i])]))
    y.append(temp)
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