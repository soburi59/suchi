 # -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:10:52 2022
"""
import pivot as pt
import numpy as np
#変数の初期化
i=0
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

#行列計算と結合ができるのでnumpyにする
data=np.array(data)
#ピボット選択
data=pt.part_pivot(data,n)
#分割
c=np.array(data[:,:-1])
b=np.array(data[:,-1])
i_np=np.array([[0.]*n]*n)
#解格納用
x=np.array([0.]*n)
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
    #途中経過行列
    #print(c)
    #print("")

for i in range(n):
    x[i]=0
    for j in range(n):
        x[i]+=c[i,n+j]*b[j]
    #表示
    print(f"x({i+1}):{round(x[i],2)}")
