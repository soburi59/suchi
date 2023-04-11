# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:20:43 2023
"""
from simulate_pendulum import *
# パラメータの設定
l = 0.5
m = 1
k = 1
g = 9.80665
theta_0 = 1
theta_dot_0 = 0
t_f = 0
t_e = 15

# hのリスト
h_list = [0.05, 0.02, 0.001]

# hごとにグラフを描画する
for h in h_list:
    theta = simulate_pendulum(l, m, k, g, theta_0, theta_dot_0, t_f, t_e, h)
    t = np.linspace(t_f, t_e, len(theta))
    plt.plot(t, theta, label=f"h={h}")

# グラフの設定
plt.xlabel("Time[sec]")
plt.ylabel("θ[rad]")
plt.title("Simulation of a pendulum using the Euler method")
plt.legend()
plt.savefig("./out/ex1-1-out.png")