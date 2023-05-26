# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:12:09 2021

@author: SNIPER
"""

def gradingStudents(grades):
    res=[]
    for i in grades:
        
        if(i>=38):
            mod5=i%5
            
            if(mod5>=3):
                i+=(5-mod5)
        res.append(i)
    print(res)
        
                
    
grades=[73,67,38,33]
gradingStudents(grades)