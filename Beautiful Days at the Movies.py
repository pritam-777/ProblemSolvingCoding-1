# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:52:18 2021

@author: SNIPER
"""

def beautifulDays(i, j, k):
    
   count=0
   for i in range(i,j):
       
       rev=0,
       while i!=0:
           r=i%10
           rev=rev*10+r
           i//10
    diff=abs(i-rev)
    if(diff%k==0):
        
            
        count+=1
    print(count)
        
            
        
   
    
    
    
    
i=20
j=23
k=6
x=beautifulDays(i, j, k)
print(x)