# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:54:52 2023

"""
import numpy as np
import matplotlib.pyplot as plt
from simulate_i import *

p = {
    'R' : 1.0, 
    'L' : 0.5,  
    'C' : 0.2,
    'u' : 1.0,
    't_f' : 0.0,  # 開始時刻
    't_e' : 10.0,  # 終了時刻
    'h' : 0.001 # 刻み幅
}

y,t = simulate_rlc_i(p)
plt.plot(t, y, label=f"R={p['R']},L={p['L']},C={p['C']}")


p['R']=1.5
p['L']=0.8
p['C']=0.8
y,t = simulate_rlc_i(p)
plt.plot(t, y, label=f"R={p['R']},L={p['L']},C={p['C']}")

p['R']=2
p['L']=1
p['C']=1
y,t = simulate_rlc_i(p)
plt.plot(t, y, label=f"R={p['R']},L={p['L']},C={p['C']}")

# グラフのプロット
plt.xlabel('t[sec]')
plt.ylabel('y(t)[V]')
plt.title("Simulating an RLC series circuit using Euler's method")
plt.grid(True)
plt.legend()
plt.savefig(f"./out/ex2-1-out.png")
