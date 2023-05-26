# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:39:21 2021

@author: SNIPER
"""

def reversedict(input_dict):
    for i in range (len(input_dict)):
        i.values().reverse()
        

input_dict = [{"name":"ragas","sex":"male"},{"name":"amos","sex":"female"}]
print(input_dict.keys())