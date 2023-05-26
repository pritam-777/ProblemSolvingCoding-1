# -*- coding: utf-8 -*-
"""
Created on Mon May 24 20:12:38 2021

@author: SNIPER
"""


def saveThePrisoner(n, m, s):
    
    r= m%n
    if(r+s-1)%n == 0:
        return n
    else:
        return r+s-1
    
    
    
    


n=7
m=19
s=2
saveThePrisoner(n, m, s)
    