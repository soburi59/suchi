# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:20:43 2023
"""
from simulate_pendulum import *
import matplotlib.pyplot as plt
import numpy as np

def sim_pendulum_plot(p, which_is_list, filename):
    print(p)
    # リスト型の引数
    list_type_var = p[which_is_list]
    plt.figure()
    
    # シミュレーションの実行
    for var in list_type_var:
        p[which_is_list] = var
        print(p)
        theta,t = simulate_pendulum(p)
        plt.plot(t, theta, label=f"{which_is_list}={var}")
    plt.xlabel("t[sec]")
    plt.ylabel("θ[rad]")
    plt.title("Simulation of a pendulum using the Euler method")
    plt.grid(True)
    plt.legend()
    plt.savefig(f"./out/{filename}")
    
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
    sim_pendulum_plot(parameters, 'h' , 'ex1-1-out.png')
