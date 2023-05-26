# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:08:57 2021

@author: SNIPER
"""

def Min_Max(arr):
    min_arr = arr[0]
    max_arr = arr[0]
    for i in range(len(arr)):
        if(arr[i]<min_arr):
            min_arr=arr[i]
        if(arr[i]>max_arr):
            max_arr=arr[i]
            
    s=sum(arr)
    minimum = s-max_arr
    maximum = s-min_arr
    print(minimum)
    print(maximum)
    
    
        
                    
     
    
    
    
    
    
arr=[1 ,2 ,3 ,4 ,5]
Min_Max(arr)
