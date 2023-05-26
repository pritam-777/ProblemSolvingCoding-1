# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:04:33 2021

@author: SNIPER
"""

def reversestring(name):
    
  
    s=""
    for i in name:
        s=i+s
        
    return s
        
        
    
    
    
    
name="pritam"
print(reversestring(name))