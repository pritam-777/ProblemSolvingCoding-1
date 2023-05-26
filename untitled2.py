# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 19:50:39 2021

@author: SNIPER
"""

def mergelist(ls1,ls2):
    lst=[]
    for i in ls1:
        if i not in lst:
            lst.append(i)
    for i in ls2:
        if i not in lst:
            lst.append(i)
    return lst
    
    
    
    

ls1=[1,1,2,3,4,5]
    
ls2=[2,2,3,4,5,6,6,7]
    
print(mergelist(ls1,ls2))