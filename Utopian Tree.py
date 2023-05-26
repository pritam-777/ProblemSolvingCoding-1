# -*- coding: utf-8 -*-
"""
Created on Wed May 12 20:41:34 2021

@author: SNIPER
"""

def utopianTree(n):
    height = 1
    for i in range(n-1):
        if(i%2==0):
            height+=1
        else:
            height*=2
    print(height)
    
    
    
n=4
utopianTree(n)

            