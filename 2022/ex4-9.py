"""
Created on Wed Jan 25 15:31:57 2023
coding: utf-8
ex4-9
"""
import numpy as np
from power_method import power_method
A=[[1,3,2],[3,5,-1],[2,-1,3]]
x=[[1],[-1],[0]]
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