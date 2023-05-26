# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 20:37:51 2021

@author: SNIPER
"""

def hello(string,k):
    char=[]
    for i in range(len(string)):
        temp=ord(string[i])-k
        char.append(chr(temp))
        listToStr = ' '.join(map(str, char))
        listToStr = ''.join(listToStr.split())
    print(listToStr)
        
        
hello("DGEO",3)