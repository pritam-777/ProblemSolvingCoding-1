# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:41:07 2021

@author: SNIPER
"""

def designerPdfViewer(h, word):
    pos=0
    maxValue=0
   
    for i in range(len(word)):
        
        pos=ord(word[i])-97
        if(h[pos]>maxValue):
            maxValue=h[pos]
            
        return len(word)*maxValue
        
    
            
        
        
         
        
    
    
    
    
    
    
h=[1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word="zaba"
t=designerPdfViewer(h,word)
print(t)