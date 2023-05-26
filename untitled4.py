# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:12:30 2021

@author: SNIPER
"""

import cv2
import numpy as np 
img = cv2.imread("MicrosoftTeams-image.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
x,y=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,3,3,91)
cv2.imshow("Binary Thresholding",y)
cv2.waitKey()
cv2.destroyAllWindows()


crop_image=img[300:400,500:700]
cv2.imshow("crop image",crop_image)
cv2.waitKey()
cv2.destroyAllWindows()