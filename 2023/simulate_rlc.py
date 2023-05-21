"""
Created on Sun May 21 20:23:51 2023
coding: utf-8

"""

import numpy as np

def simulate_rlc(p):
    R = p['R']
    L = p['L']
    C = p['C']
    u = p['u']
    t_e = p['t_e']
    h = p['h']
    y = [0.0]
    y_dot = 0.0
    t = [p['t_f']]

    # オイラー法で微分方程式を解く
    i = 0
    while t[i] <= t_e:
        # オイラー法による更新式
        y_ddot = (1 / L / C) * u - (R / L) * y_dot - (1 / L / C) * y[i]
        y_dot += h * y_ddot
        y.append(y[i] + h * y_dot)
        t.append(t[i] + h)
        i+=1
    return y,t
