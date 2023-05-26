# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:35:43 2021

@author: SNIPER
"""

from collections import Counter

def sockMerchant(ar):
    s=0
    for i in Counter(ar).values():
        s+=i//2
        
    print(s)
    
    
    
ar=[10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(ar)

        