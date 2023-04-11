# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 09:52:19 2022
ex4.8
"""
import numpy as np
from power_method import power_method
A=[[4,1],[1,0]]
x=[[0],[1]]
b=power_method(A,x)
#print(A-b[1]*b[1].T)
b=power_method(A-b[0]*b[1]*b[1].T,x)
print(f"固有値lambda2:{b[0]}")
print(f"固有ベクトルx2:\n{b[1]}")