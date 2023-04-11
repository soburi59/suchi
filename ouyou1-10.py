import sympy as sp
import math
from matplotlib import pyplot as plt
import numpy as np

#宣言,定義
k=0
n=5
x0=0
x=sp.Symbol('x',real=True)
func=sp.log(1+x)
#目盛り
gx=list(np.arange(-0.9,5.1,0.1))
#結果用の空配列
gy=[]

#設定系(自己満)
#線を内側に
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#空のグラフを作っとく
fig = plt.figure()
ax = fig.add_subplot(111)
#上下左右に目盛り
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
#ラベル
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
#目盛りをいじる
ax.set_xlim(-1, 5)
ax.set_ylim(-5, 5)
ax.set_xticks(range(-1,6))
ax.set_yticks(range(-5,6))

#本来の関数グラフ
ax.plot(gx,[sp.log(i+1) for i in gx],label="Original",color="black")

#1次から5次までテイラー展開し,結果を2次配列に格納するとともに,プロットする
for i in range(1,n+1):
    taylor=0
    #剰余項が邪魔なのでremoveOで排除
    taylor=sp.series(func, x, x0, i+1).removeO()
    '''
    #seriesを使わずに自力でやる場合
    for k in range(i+1):
        taylor+=sp.diff(func,x,k).subs(x,x0)*((x-x0)**k)/math.factorial(k)
    '''
    print(f"{i}次:{taylor}")
    #結果を配列に挿入
    gy.append([float(taylor.subs(x,k)) for k in gx])
    ax.plot(gx,gy[i-1],label=str(i)+"series")

#表示
plt.legend(loc="lower left")
plt.show()

del gx,gy,taylor