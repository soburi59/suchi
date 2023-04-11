# -*- coding: utf-8 -*-
"""
3.3
境界値問題
Created on Tue Nov  8 10:03:28 2022
"""
from matplotlib import pyplot as plt
import pivot as pt
import numpy as np
import sympy as sp
#分割数
N=10
#初期条件
x_first=0
x_last=1
y_first=0
y_last=0.25
h=(x_last-x_first)/N
a=sp.Symbol('a',real=True)
#解析解
f=(1/4)*(sp.exp(2*a)-sp.exp(-2*a))/(sp.exp(2)-sp.exp(-2))
#変数の初期化
i=0
#ファイル入力
with open('input.txt') as file:
    for s_line in file:
        #1行を空白区切りで分割しリスト化
        str=s_line.split()
        if i == 0:
            #初回ループのみ初期化
            n=len(str)-1
            data=[[]]*n
        #floatに変換
        data[i]=[float(x) for x in str]
        i+=1
#行列計算と結合ができるのでnumpyにする
data=np.array(data)
#ピボット選択
data=pt.part_pivot(data,n)
#分割
c=np.array(data[:,:-1])
b=np.array(data[:,-1])
i_np=np.array([[0.]*n]*n)
#解格納用
y=np.array([0.]*n)
x=np.arange(0,x_last+h,h)
#単位行列
for i in range(n):
    i_np[i,i]=1
#拡大行列
c=np.concatenate([c,i_np],1)

#以降使わないので一応メモリ解放
del data
del i_np
del str
for k in range(n):
    temp=c[k,k]
    for j in range(2*n):
        c[k,j]/=temp
    for i in range(n):
        if i==k:
            continue
        temp=c[i,k]
        for j in range(k,2*n):
            c[i,j]-=c[k,j]*temp

for i in range(n):
    for j in range(n):
        y[i]+=c[i,n+j]*b[j]


#先頭と末尾に初期条件を挿入
y=np.insert(y,0,y_first)
y=np.append(y,y_last)

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
y_=[f.subs(a,i) for i in x]
ax.plot(x,y,label="boundary value")
ax.plot(x,y_,label="answer")
gosalist=[abs(i-j) for i,j in zip(y,y_)]
ax2 = fig.add_subplot(2,1,2)
ax2.plot(x[1:-1],gosalist[1:-1],label="measurement error")
ax2.legend()
for i in range(len(y)):
    print(f"y_true({i}):{round(float(y_[i]),6)},y({i}):{round(y[i],6)}")
ax.legend()

