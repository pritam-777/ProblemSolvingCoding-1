# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:53:05 2021

@author: SNIPER
"""

def countingValleys(steps, path):
    count=0
    result=0
    for i in path:
        if i == 'U':
            count+=1
        else:
            count-=1
        if(count==0 and i=='U'):
            result+=1
    print(result)
   
    
    
    
    
    
steps = 8
path ="UDDDUDUU"
countingValleys(steps,path)