# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:09:14 2023

"""

import numpy as np

# 行列Aを定義
A = np.array([[4,1],[1,0]])

# 初期値として適当なベクトルを決める
x = np.array([1, 1])

# 繰り返し回数
n = 100

for i in range(n):
    # 初期値を行列Aにかける
    x = np.dot(A, x)
    # 大きさを正規化
    x = x / np.linalg.norm(x)

# 固有値
eig_val = np.dot(x, np.dot(A, x))

# 固有ベクトル
eig_vec = x

# 結果を表示
print("固有値:", eig_val)
print("固有ベクトル:", eig_vec)