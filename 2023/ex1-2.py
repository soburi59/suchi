"""
Created on Thu May 18 19:25:06 2023
coding: utf-8

"""
from simulate_pendulum import *
from plot_simulate import *
p = dict()
def init_p():
    global p
    p = {
        'l' : 1, # 糸の長さ
        'm' : 1.0,  # 重りの重さ
        'k' : 1.0,  # 粘性減衰係数
        'g' : 9.80665,  # 重力加速度
        'theta_0' : 1.0,  # 振り子の初期角度
        'theta_dot_0' : 0.0,  # 角速度の初期値
        't_f' : 0.0,  # 開始時刻
        't_e' : 15.0,  # 終了時刻
        'h' : 0.001 # 刻み幅
    }
init_p()
simu=simulation_comparison_plot

init_p()
p['l']=[0.5,1,1.5]
simu(p,'l','ex1-2-l-out.png')

init_p()
p['m']=[0.5,1,1.5]
simu(p,'m','ex1-2-m-out')

init_p()
p['k']=[0.5,1,1.5]
simu(p,'k','ex1-2-k-out.png')

init_p()
p[]
