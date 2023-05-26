# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 20:52:08 2021

@author: SNIPER
"""

def breakRecords(scores):
    
    highScores = scores[0]
    lowScores = scores[0]
    
    CountHighScores=0
    CountLowScores=0
    
    for i in range (len(scores)):
        if(scores[i]<lowScores):
            lowScores=scores[i]
            CountLowScores+=1
        elif(scores[i]>highScores):
            highScores=scores[i]
            CountHighScores+=1
            
    print(CountHighScores,CountLowScores)
    
    
    
    
arr=[3 ,4 ,21, 36, 10, 28, 35, 5, 24, 42]
breakRecords(arr)
        
    