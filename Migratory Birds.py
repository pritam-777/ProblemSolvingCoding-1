# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 20:09:19 2021

@author: SNIPER
"""

def migratoryBirds(arr):
    n=[0]*len(arr)
    for i in range(len(arr)):
        n[arr[i]]+=1
    print(n.index(max(n)))
        
    
        
        
        
arr=[1, 4, 4, 4, 5, 3]   
migratoryBirds(arr)    