# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:16:12 2021

@author: SNIPER
"""

def Compare(a,b):

   count_a=0
   count_b=0
   for i in range (len(a)):
        if(a[i]>b[i]):
            count_a+=1
        elif(a[i]<b[i]):
            count_b+=1
   print(count_a,count_b)
       
       
    
    
    
    
    
    
    
    
    
a=[17 ,28 ,30]
b=[99 ,16 ,8]
Compare(a,b)