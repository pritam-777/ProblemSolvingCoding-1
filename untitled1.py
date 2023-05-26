# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:31:23 2021

@author: SNIPER
"""



def BinarySerach(arr,l,n,x):
    l=0
    r=n-1
    if l<r:
         mid = (r+l)//2
         if(arr[mid]==x):
             return mid
         elif(arr[mid]<n):
             return BinarySerach(arr,mid+1,r,x)
         else:
             return BinarySerach(arr,l,mid,x)
    else:
        return -1
         
            
arr=[34,47,68,87,111,139,231]
x=34
n=len(arr)
se=BinarySerach(arr,0,n,x)
print(se)
ls=[1,2,3,5,6]
