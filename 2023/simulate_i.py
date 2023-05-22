# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:54:23 2023

"""

import numpy as np

def simulate_rlc_i(p):
    R = p['R']
    L = p['L']
    C = p['C']
    u = p['u']
    t_e = p['t_e']
    h = p['h']
    i = [0.0]
    i_dot = 0.0
    t = [p['t_f']]

    # オイラー法で微分方程式を解く
    n = 0
    while t[n] <= t_e:
        # オイラー法による更新式
        i_ddot = (1 / L) * u - (R / L) * i_dot - (1 / L / C) * i[n]
        i_dot += h * i_ddot
        i.append(i[n] + h * i_dot)
        t.append(t[n] + h)
        n += 1
    return i, t
