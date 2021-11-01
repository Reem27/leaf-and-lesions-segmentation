# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:07:14 2021

@author: x16
"""
import cv2

import matplotlib.pyplot as plt
import collections, numpy as np
img = cv2.imread("C:/Users/x16/Desktop/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/leaf/train/dataset2/tested/maskedDSC_4080.jpg")
img2= cv2.imread("C:/Users/x16/Desktop/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/leaf/train/dataset2/tested/maskedDSC_4080.jpg", 0)

height, width, channels = img.shape
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array ([60, 76, 48])#np.array ([23, 76, 66]) for whiteboard dataset
lighter = np.array ([119, 160, 153])
mask = cv2.inRange(hsv, lower, lighter)
res = cv2.bitwise_and(img,img, mask= mask)    
#resb,resg,resr = cv2.split(res)        
b,g,r = cv2.split(img) 
#imgg = cv2.merge((b,g,r))                
#res= cv2.merge((resb,resg,resr))  
#bb,gg,rr = cv2.split(imgg)
cv2.imshow("res",res)
        
"""""
sigma = 0.3
median = np.median(imgg)           
lower = int(max(0, (1.0 - sigma) * median))
upper = int(min(255, (1.0 + sigma) * median)) 
auto_canny = cv2.Canny(imgg, lower, upper)
"""
                             
               
########################################################
#bb,gg,rr = cv2.split(imgg)     
cv2.imshow('original',img)
cv2.imshow('mask',mask)
cv2.imshow('noise',res)
#cv2.imshow('cell',cells)
#cv2.imshow('no noise',img2)
#cv2.imshow('auto_canny',auto_canny)
cv2.waitKey(0)
cv2.destroyAllWindows() 