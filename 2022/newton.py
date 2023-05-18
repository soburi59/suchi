# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:25:27 2022
newton method for non-linear equations
"""
import sympy as sp
import numpy as np
from matplotlib import pyplot as plt
k=0
X=[3]
dX=[]
eps=10**-5
#変数用
x=sp.Symbol('x',real=True)
num=int(input("近似する平方根(整数):"))
original=sp.sqrt(num)

func=(x**2)-(original**2)

while True:
    k+=1
    dX.append(sp.diff(func))
    temp=func.subs(x,X[k-1])/dX[k-1].subs(x,X[k-1])
    X.append(X[k-1]-temp)
    if abs((X[k]-X[k-1])/X[k])<eps:
        break
    if abs(X[k]-X[k-1])>abs(X[k-1]-X[k-2]):
        break
print(f"反復回数:{k}")
print(f"近似値:{round(X[k],5)}")

#plot------------------------
#目盛り
gx=list(np.arange(X[0]-2,X[0]+2,0.1,dtype=float))


#線を内側に
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#空のグラフを作っとく
fig, ax = plt.subplots()
#上下左右に目盛り
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
#ラベル
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
#目盛りをいじる
ax.set_xlim(X[0]-2,X[0]+2)
ax.set_ylim(-1,2)
ax.set_xticks(np.arange(X[0]-2,X[0]+2,0.5,dtype=float))
ax.set_yticks(range(-1,2))
#座標軸表示
ax.axhline(c="black",linewidth=0.5)
#本来の関数グラフ
ax.plot(gx,[func.subs(x,i) for i in gx],label="Original",color="black")
for i in range(len(dX)):
    ax.plot( [X[i+1],X[i]] , [0,func.subs(x,X[i])],ls="dotted" )
    ax.plot([X[i],X[i]],[0,func.subs(x,X[i])],ls="dotted")
#表示
plt.legend()
plt.show()
