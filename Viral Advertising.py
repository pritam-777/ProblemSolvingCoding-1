# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:36:55 2021

@author: SNIPER
"""

def viralAdvertising(n):
    total_liked =0
    share=5
    liked=0
    for i in range(n):
        
        liked = share//2
        total_liked+=total_liked
        share=liked*3
        
    print(total_liked)
    
    
n=5    
viralAdvertising(n)
        
        