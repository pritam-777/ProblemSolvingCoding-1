# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:51:24 2021

@author: SNIPER
"""

def bonAppetit(bill, k, b):
    s=sum(bill)
    charges=(s-bill[k])//2
    if(charges==b):
        print("Bon Appetit")
    else:
        print(b-charges)
    
    
    
    
    
      
        
    
    
    
    
bill =[3,10,2,9]
k=1
b=12
bonAppetit(bill, k, b)
 