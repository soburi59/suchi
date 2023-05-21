"""
Created on Sun May 21 20:36:58 2023
coding: utf-8

"""

import numpy as np
import matplotlib.pyplot as plt
from simulate_rlc import *

p = {
    'R' : 1.0, 
    'L' : 0.5,  
    'C' : 0.2,
    'u' : 1.0,
    't_f' : 0.0,  # 開始時刻
    't_e' : 10.0,  # 終了時刻
    'h' : 0.001 # 刻み幅
}

y,t = simulate_rlc(p)
plt.plot(t, y, label=f"R={p['R']},L={p['L']},C={p['C']}")


p['R']=1.5
p['L']=0.8
p['C']=0.8
y,t = simulate_rlc(p)
plt.plot(t, y, label=f"R={p['R']},L={p['L']},C={p['C']}")

p['R']=2
p['L']=1
p['C']=1
y,t = simulate_rlc(p)
plt.plot(t, y, label=f"R={p['R']},L={p['L']},C={p['C']}")

# グラフのプロット
plt.xlabel('t[sec]')
plt.ylabel('y(t)[V]')
plt.title("Simulating an RLC series circuit using Euler's method")
plt.grid(True)
plt.legend()
plt.savefig(f"./out/ex2-1-out.png")
