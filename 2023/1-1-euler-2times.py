# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:34:19 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# 時間の範囲を設定
t0 = 0
tf = 15

# 刻み幅のリスト
h_list = [0.001, 0.02, 0.05]

# 微分方程式のパラメータ
l = 0.5
m = 1
k = 1

# 初期条件
theta0 = 1
theta_dot0 = 0

for h in h_list:
    # 時間ステップ
    n = int((tf - t0) / h)

    # 時間と角度を格納する配列を作成
    t = np.zeros(n+1)
    theta = np.zeros(n+1)

    # 初期条件を設定
    t[0] = t0
    theta[0] = theta0

    # オイラー法で微分方程式を解く
    for i in range(n):
        t[i+1] = t[i] + h
        theta[i+1] = theta[i] + h*theta_dot0
        theta_dot0 -= h*(k/m)*np.sin(theta[i])

    # グラフを描画
    plt.plot(t, theta, label=f"h={h}")

# グラフの設定
plt.xlabel("Time")
plt.ylabel("Angle")
plt.title("Simulation of Simple Pendulum")
plt.legend()
plt.show()
