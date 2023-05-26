# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 19:24:21 2021

@author: SNIPER
"""

def catAndMouse(x, y, z):
    
    distanceXZ=x-z
    distanceYZ=y-z
    if(distanceXZ<distanceYZ):
        return "Cat A"
    elif(distanceXZ==distanceYZ):
        print("Mouse C")
    else:
        print("Cat B")
    
    
    
    
    x=2
    y=5
    z=4
    
    catAndMouse(x, y, z)
    