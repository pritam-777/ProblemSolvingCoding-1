# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:06:59 2021

@author: SNIPER
"""
from functools import reduce

def getTotalX(a, b):
    def GCD(a,b):
        if(b==0):
            return a
        return GCD(b,a%b)
    def LCM(a,b):
        return (a*b)//GCD(a,b)
    l=reduce(LCM,a)
    g=reduce(GCD,a)
    s=0
    for i in range(l,g+1,l):
        if g%i==0:
            s+=1
        return s
    
    
    
    
a=[2,6]
b=[24,36]
print(getTotalX(a,b))