# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:19:51 2021

@author: SNIPER
"""

def BinarySearch(Arr,l,r,x):
    if r>=l:
        mid = l+(r-l)//2
        if(Arr[mid]==x):
            return mid
        elif Arr[mid]<x:
            return BinarySearch(Arr,mid+1,r,x)
        else:
            return BinarySearch(Arr,l,mid-1,x)
    else:
        return -1
    
    
    
Arr=[34,47,68,87,111,139,231]
x= 68
res = BinarySearch(Arr,0,len(Arr)-1,x)