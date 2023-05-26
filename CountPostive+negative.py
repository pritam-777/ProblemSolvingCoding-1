# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 19:48:12 2021

@author: SNIPER
"""
x =[2,3,-4,0,5,-1,-1,-4]
count_positive=0
count_negative=0
count_zero=0

for i in range (len(x)):
    
    if(x[i]>0):
        count_positive+=1
    elif(x[i]<0):
        count_negative+=1
    else:
        count_zero+=1
        


print(count_positive/len(x))
print(count_negative/len(x))
print(count_zero/len(x))
   