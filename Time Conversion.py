# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:52:52 2021

@author: SNIPER
"""
def timeConversion(s):
    t = s.split(":")
    if(s[-2:]=="PM"):
        if(t[0]!="12"):
            t[0]=str(int(t[0])+12)
    else:
        if(t[0]=="12"):
            t[0]="00"
    ntime = ':'.join(t)
        
    print(ntime)
            
    





s = "07:05:45PM"
timeConversion(s)

