# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 20:09:01 2021

@author: SNIPER
"""

def Diagonal_Difference(arr):
    n = len(arr)
    di_1 = 0
    di_2 = 0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                print(arr[i][j])
                di_1+=arr[i][j]
            if(i==n-j-1):
                print(i)
                print(arr[i][j])
                di_2+=arr[i][j]
                
                
    return abs(di_1-di_2)
    
    
    
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
    
res=Diagonal_Difference(arr)
print(res)