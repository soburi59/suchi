# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:31:39 2023
ex4.4
"""
import numpy as np
from power_method import power_method
A=[[1,3,2],[3,5,-1],[2,-1,3]]
x=[[1],[-1],[0]]
b=power_method(A,x)
print(f"固有値lambda:{b[0]}")
print(f"固有ベクトルx:\n{b[1]}")