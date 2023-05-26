# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:18:29 2021

@author: SNIPER
"""

def high(arr):
    max_elements = max(arr)
    count=0
    for i in range(len(arr)):
        if(arr[i]==max_elements):
            count+=1
    print(count)
    
    
    
#arr=[4,2,4,1]
arr1=[18,90,90 ,13 ,90 ,75 ,90 ,8 ,90, 43]
arr2=[3, 2 ,1, 3]
high(arr2)