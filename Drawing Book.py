# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:28:25 2021

@author: SNIPER
"""

def pageCount(n,p):
    l=p//2
    n=n+1 if(n%2==0)else n
    r=(n-p)//2
    print(min(l,r))
        
    


n=8
p=5
pageCount(n,p)