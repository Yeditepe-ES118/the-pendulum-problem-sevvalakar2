# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 17:29:50 2025

@author: HP
"""
import numpy as np

def find_period(L0, L1):
    g = 9.81
    T0 = 0
    T1 = 0
    
    for L in range(L0, L1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        T_rounded = np.round(T, 1)
        print(f"When L = {L}.0 m, T = {T_rounded} s")
        
        if L == L0:
            T0 = T
        if L == L1:
            T1 = T
    
    return T0, T1


