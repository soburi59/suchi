# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 16:20:43 2023
"""
from simulate_pendulum import *
import matplotlib.pyplot as plt
import numpy as np

def simulation_comparison_plot(l, m, k, g, theta_0, theta_dot_0, t_f, t_e, h, which_is_list, filename):
    # リスト型の引数
    list_type_var = locals()[which_is_list]
    
    var_name_list = list(locals().keys())
    num_loc = var_name_list.index(which_is_list)
    
    # リスト型の引数だったものを仮のものに変更
    locals()[which_is_list] = 0
    
    # シミュレーション結果を格納するリスト
    results = []
    
    plt.figure()
    
    # シミュレーションの実行
    params = [l, m, k, g, theta_0, theta_dot_0, t_f, t_e, h]
    for var in list_type_var:
        params[num_loc] = var
        theta = simulate_pendulum(*params)
        t = np.arange(t_f, t_e, h)
        plt.plot(t, theta, label=f"{which_is_list}={var}")
        params[i] = var_dict[which_is_list]  # パラメータを元に戻す
    plt.xlabel("Time [sec]")
    plt.ylabel("θ [rad]")
    plt.title("Simulation of a pendulum using the Euler method")
    plt.legend()
    plt.savefig(f"./out/{filename}")

    

# パラメータの設定
l = 0.5 # 糸の長さ
m = 1.0  # 重りの重さ
k = 1.0  # 粘性減衰係数
g = 9.80665  # 重力加速度
theta_0 = 1.0  # 振り子の初期角度
theta_dot_0 = 0.0  # 角速度の初期値
t_f = 0.0  # 開始時刻
t_e = 15.0  # 終了時刻
# hのリスト
h = [0.05, 0.02, 0.001]
simulation_comparison_plot(l, m, k, g, theta_0, theta_dot_0, t_f, t_e, h, 'h' , 'ex1-1-out.png')
