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
g = 9.80665

# 初期条件
theta0 = 1
theta_dot0 = 0

for h in h_list:
    # 時間ステップ
    n = int((tf - t0) / h)

    # 時間と角度を格納する配列を作成
    t = np.linspace(t0, tf, n+1)
    theta = np.zeros(n+1)
    theta_dot = np.zeros(n+1)
    theta[0] = theta0
    theta_dot[0] = theta_dot0

    # オイラー法で微分方程式を解く
    for i in range(n):
        theta_ddot = -(k/m)*theta_dot[i] - (g/l)*np.sin(theta[i])
        theta_dot[i+1] = theta_dot[i] + h*theta_ddot
        theta[i+1] = theta[i] + h*theta_dot[i]

    # グラフを描画
    plt.plot(t, theta, label=f"h={h}")

# グラフの設定
plt.xlabel("Time[sec]")
plt.ylabel("θ[rad]")
plt.title("Simulation of a pendulum using the Euler method")
plt.legend()
plt.show()
