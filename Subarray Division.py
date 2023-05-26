# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:19:19 2021

@author: SNIPER
"""

def birthday(s, d, m):
    count=0
    for i in range (len(s)):
        
        if i+m<=len(s):
            temp=sum(s[i:i+m])
            if(temp==d):
                count+=1
    print(count)
        
    
    
    
    
    
    
    
    
    
s=[1 ,2, 1, 3, 2]
d=3
m=2
birthday(s,d,m)