import pivot as pt
import numpy as np
#                1,2,3,4,5,6,7,8,9,0,1,2,b
data=np.array([[-4,1,0,1,0,0,0,0,0,0,0,0,-100],
               [1,-4,1,0,1,0,0,0,0,0,0,0,-100],
               [0,1,-4,0,0,1,0,0,0,0,0,0,-100],
               [1,0,0,-4,1,0,1,0,0,0,0,0,0],
               [0,1,0,1,-4,1,0,1,0,0,0,0,0],
               [0,0,1,0,1,-4,0,0,1,0,0,0,0],
               [0,0,0,1,0,0,-4,1,0,1,0,0,0],
               [0,0,0,0,1,0,1,-4,1,0,1,0,0],
               [0,0,0,0,0,1,0,1,-4,0,0,1,0],
               [0,0,0,0,0,0,1,0,0,-4,1,0,100],
               [0,0,0,0,0,0,0,1,0,1,-4,1,100],
               [0,0,0,0,0,0,0,0,1,0,1,-4,100]
               ],dtype="float64")
n=12

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
    print(c)
    print("")

for i in range(n):
    x[i]=0
    for j in range(n):
        x[i]+=c[i,n+j]*b[j]
    #表示
    print(f"x({i+1}):{round(x[i],3)}")
