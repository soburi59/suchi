# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:46:16 2023
"""
from plot_simulate import *

# パラメータの設定
l = 1 # 糸の長さ
m = 1  # 重りの重さ
k = 1  # 粘性減衰係数
g = 9.80665  # 重力加速度
theta_0 = 1  # 振り子の初期角度
theta_dot_0 = 0  # 角速度の初期値
t_f = 0  # 開始時刻
t_e = 15  # 終了時刻
h = 0.001 #刻み

simulation_comparison_plot([l-0.5,l,l+0.5], m, k, g, theta_0, theta_dot_0, t_f, t_e, h, 'h', 'ex1-2-l-out.png')
simulation_comparison_plot(l, [m-0.5,m,m+0.5], k, g, theta_0, theta_dot_0, t_f, t_e, h, 'h', 'ex1-2-m-out.png')
