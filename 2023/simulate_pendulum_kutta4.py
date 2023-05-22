# -*- coding: utf-8 -*-
"""
Created on Mon May 22 15:23:14 2023
4 dim
"""

import numpy as np
from plot_simulate import *
def simulate_pendulum_kutta2(p):
    l = p['l']
    m = p['m']
    k = p['k']
    g = p['g']
    theta_dot = p['theta_dot']
    t_f = p['t_f']
    t_e = p['t_e']
    h = p['h']

    theta = [p['theta']]
    t = [t_f]

    # 4次のルンゲ・クッタ法で微分方程式を解く
    i = 0
    while t[i] <= t_e:
        k1_theta_dot = h * theta_dot
        k1_theta_ddot = h * (-(k / m) * theta_dot - (g / l) * np.sin(theta[i]))

        k2_theta_dot = h * (theta_dot + 0.5 * k1_theta_ddot)
        k2_theta_ddot = h * (-(k / m) * (theta_dot + 0.5 * k1_theta_ddot) - (g / l) * np.sin(theta[i] + 0.5 * k1_theta_dot))

        k3_theta_dot = h * (theta_dot + 0.5 * k2_theta_ddot)
        k3_theta_ddot = h * (-(k / m) * (theta_dot + 0.5 * k2_theta_ddot) - (g / l) * np.sin(theta[i] + 0.5 * k2_theta_dot))

        k4_theta_dot = h * (theta_dot + k3_theta_ddot)
        k4_theta_ddot = h * (-(k / m) * (theta_dot + k3_theta_ddot) - (g / l) * np.sin(theta[i] + k3_theta_dot))

        theta_dot += (1 / 6) * (k1_theta_ddot + 2 * k2_theta_ddot + 2 * k3_theta_ddot + k4_theta_ddot)
        theta.append(theta[i] + (1 / 6) * (k1_theta_dot + 2 * k2_theta_dot + 2 * k3_theta_dot + k4_theta_dot))
        t.append(t[i] + h)
        i += 1

    return theta, t

if __name__=='__main__':
    parameters = {
        'l' : 0.5, # 糸の長さ
        'm' : 1.0,  # 重りの重さ
        'k' : 1.0,  # 粘性減衰係数
        'g' : 9.80665,  # 重力加速度
        'theta' : 1.0,  # 振り子の初期角度
        'theta_dot' : 0.0,  # 角速度の初期値
        't_f' : 0.0,  # 開始時刻
        't_e' : 15.0,  # 終了時刻
        # hのリスト
        'h' : [0.05, 0.02, 0.001]
    }
    sim_pendulum_plot(parameters, 'h' , 'ex1-3-4out.png')