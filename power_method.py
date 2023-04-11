# -*- coding: utf-8 -*-
"""
べき乗法
Created on Tue Dec 20 09:52:19 2022
and ex4.3
"""
import numpy as np
def power_method(A,x):
    i=0
    x=np.matrix(x)
    A=np.matrix(A)
    ips=10**-10
    lamb=[1]
    k=0
    #--------
    while True:
        u=A*x
        lamb.append(float(x.T*u))
        x=u/np.linalg.norm(u)
        k+=1
        if abs(lamb[k]-lamb[k-1])<ips:
            break
    return [round(lamb[-1],3),x]

if __name__ == '__main__':
    A=[[4,1],[1,0]]
    x=[[0],[1]]
    b=power_method(A,x)
    print(f"固有値lambda:{b[0]}")
    print(f"固有ベクトルx:\n{b[1]}")