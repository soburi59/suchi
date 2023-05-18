"""
Created on Wed Jan 25 16:24:59 2023
coding: utf-8
ex4-10
"""

import numpy as np
from power_method import power_method
A=[[3,0,0,1],[0,3,0,0],[0,0,1,0],[1,0,0,3]]
x=[[12],[1],[7],[1]]
b=power_method(A,x)
W1=A-b[0]*b[1]*b[1].T
#print(W1)
b=power_method(W1,x)
print(f"固有値lambda2:{b[0]}")
print(f"固有ベクトルx2:\n{b[1]}")
W2=W1-b[0]*b[1]*b[1].T
#print(W2)
b=power_method(W2,x)
print(f"固有値lambda3:{b[0]}")
print(f"固有ベクトルx3:\n{b[1]}")
W3=W2-b[0]*b[1]*b[1].T
#print(W3)
b=power_method(W3,x)
print(f"固有値lambda4:{b[0]}")
print(f"固有ベクトルx4:\n{b[1]}")
