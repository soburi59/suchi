# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:14:43 2022
"""
import numpy as np
def part_pivot(data,n):
    
    i=0
    for i in range(n):
        #各列の最大値の位置を探す
        max_pos=np.argmax(np.abs(data[i:,i]),axis=0)+i
        #行を入れ替えるためのリスト更新
        swap_list=list(range(n))
        swap_list[i]=max_pos
        swap_list[max_pos]=i
        #実際の入替え
        data=data[swap_list]
    return data