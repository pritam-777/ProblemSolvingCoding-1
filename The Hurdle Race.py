# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:41:58 2021

@author: SNIPER
"""

def hurdleRace(k, height):
    maxHeight=height[0]
    for i in range(len(height)):
        if(height[i]>maxHeight):
            maxHeight=height[i]
    if(maxHeight>k):
        return maxHeight-k
    else:
        return 0
    
    
    
   
    
k= 7
height=[2, 5 ,4, 5, 2]
x=hurdleRace(k,height)
print(x)
     