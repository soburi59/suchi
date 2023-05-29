# -*- coding: utf-8 -*-
"""
Created on Fri May 26 11:44:04 2023

"""

import numpy as np

def rotate_point(x, y, x0, y0, theta):
    # 行列計算用の行列を定義
    matrix1 = np.array([[1, 0, 0], [0, 1, 0], [-x0, -y0, 1]])
    matrix2 = np.array([[np.cos(theta), np.sin(theta), 0], [-np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    matrix3 = np.array([[1, 0, 0], [0, 1, 0], [x0, y0, 1]])

    # 回転後の座標を計算
    transformed_point = np.dot(np.dot(np.dot([x, y, 1], matrix1), matrix2), matrix3)

    return transformed_point[0], transformed_point[1] ,transformed_point[2]

# 点(100, 20)を点(50, 50)を中心に70度左回りに回転させる
x, y, z = rotate_point(100, 20, 50, 50, np.radians(-70))

print("回転後の座標: ({}, {}, {})".format(x, y, z))
