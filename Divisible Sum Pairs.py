# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 19:51:00 2021

@author: SNIPER
"""

def  divisibleSumPairs(ar,k):
    count=0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if (ar[i]+ar[j+1]) %k==0:
                count+=1
                
    
    
arr=[1, 3, 2, 6, 1 ,2]
k=3
divisibleSumPairs(arr,k)

    
    
