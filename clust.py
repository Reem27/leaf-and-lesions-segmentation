# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 23:10:09 2021

@author: x16
"""
import cv2
import matplotlib.pyplot as plt
import collections, numpy as np
#846 #589  #1647
img = cv2.imread("images/overlap/seg/796.png")
img2= cv2.imread("images/overlap/seg/796.png", 0)
b,g,r = cv2.split(img) 
#bb,gg,rr=cv2.split(img)
#height, width, channels = img.shape
#RCP = r - img2
#GCP = g - img2
BCP = b - img2
#b,g,r = cv2.split(img) 
#sourceFile = open('35_rust.txt', 'w')
#for i in range(height):
#     for j in range(width):
#         if(BCP[i,j]!=0):
#           print( BCP[i,j], end = ' ', file = sourceFile )
#     print( (), file = sourceFile)
#sourceFile.close()     
            #if(BCP[i,j]>=130 and BCP[i,j]<= 150):
            #    bb[i,j]=b[i,j]
            #    gg[i,j]=g[i,j]
            #    rr[i,j]=r[i,j]
            #else:
            #    bb[i,j]=0
            #    gg[i,j]=0
             #   rr[i,j]=0

cv2.imshow('BCP',BCP)
cv2.imshow('img', img)
#cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()           