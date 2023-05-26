# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:48:00 2021

@author: SNIPER
"""

def angryProfessor(k, a):
    
    count=0
    for i in range(len(a)):
        if(a[i]<=0):
            count+=1
            
    if(count>=k):
        print("NO")
    else:
        print("YES")
    
    
    
    
    
    
k=3
n=[-2,-1,0,1,2]
angryProfessor(k,n)