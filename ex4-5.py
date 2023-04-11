# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:31:39 2023
ex4.5
"""
import numpy as np
from power_method import power_method
A=[[3,0,0,1],[0,3,0,0],[0,0,1,0],[1,0,0,3]]
x=[[1],[0],[0],[1]]
b=power_method(A,x)
print(f"固有値lambda:{b[0]}")
print(f"固有ベクトルx:\n{b[1]}")