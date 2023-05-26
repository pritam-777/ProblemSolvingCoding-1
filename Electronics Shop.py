# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:12:13 2021

@author: SNIPER
"""

def getMoneySpent(keyboards, drives, b):
    result=0
    no=-1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            result=keyboards[i]+drives[j]
            if(result<=b and result>no ):
                no=result
                
    print(no)
            
    
    
    
b=60
keyboards=[40,50,60]
drives=[5,8,12]
getMoneySpent(keyboards,drives,b)