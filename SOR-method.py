# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:52:35 2022

@author: 59195
"""
import numpy as np
import pivot as pt
from matplotlib import pyplot as plt
#変数の初期化
eps=10**-5
m=0
i=0
#オメガここでは1.4  (0<omg<2)
omg=1.1

#1式ごとに入力
print("入力例：3x(1)+4x(2)=5 → 3 4 5")
while True:
    #1行入力し空白区切りで分割しリスト化
    str=input(f"input({i+1}):").split()
    if i == 0:
        #初回ループのみ初期化
        n=len(str)-1
        data=[[]]*n
    #floatに変換
    data[i]=[float(x) for x in str]
    i+=1
    if i>=n :
        break

#計算はnumpyのほうが得意なので拡張性も考えnumpyにする
data=np.array(data)
data=pt.part_pivot(data,n)
a=data[:,:-1]
b=data[:,-1]
x=np.array([1.2]*n,dtype="float64")
ploty=np.array(list(x))
plotx=[0]

#以降使わないので一応メモリ解放
del str
del data

#計算
while(m<=n):
    #行についての計算
    for i in range(n):
        s=0.0
        #列についての計算
        for j in range(n):
            s+=a[i,j]*x[j]
        X=(b[i]-s+a[i,i]*x[i])/a[i,i]
        X=x[i]+omg*(X-x[i])
        temp=((X-x[i])/X)
        if temp<0:temp*=-1
        #収束判定
        if temp<eps:
            m+=1
        x[i]=X
        print(f"x({i+1}):{round(x[i],3)}")
        if i+1==n:
            print("")
    ploty=np.vstack([ploty,x])
    plotx.append(plotx[-1]+1)

#表示
for i in range(n):
    print(f"x({i+1}):{round(x[i],3)}")

#グラフ
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(n):
    ax.plot(plotx,ploty[:,i],label=f"x({i+1})",marker="o")
#ラベル
ax.set_xlabel('Number of times[times]')
ax.set_ylabel('Numerical value of the solution')
#目盛りをいじる
ax.set_xticks(list(plotx))
plt.grid()
plt.legend()
plt.show()