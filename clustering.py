# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:53:18 2021

@author: x16
"""

import cv2
import matplotlib.pyplot as plt
import collections, numpy as np
#846 #589  #1647
img = cv2.imread("C:/Users/x16/Desktop/related to dataset/FiltersandSegmentation/Watershed/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/train/dataset2/maskedDSCN1875.jpg")
img2= cv2.imread("C:/Users/x16/Desktop/related to dataset/FiltersandSegmentation/Watershed/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/train/dataset2/maskedDSCN1875.jpg", 0)
b,g,r = cv2.split(img) 
height, width, channels = img.shape
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array ([60, 76, 48])
lighter = np.array ([119, 160, 153])
mask = cv2.inRange(hsv, lower, lighter)
res = cv2.bitwise_and(img,img, mask= mask)    
resr,resg,resb = cv2.split(res)   
height, width, channels = img.shape
RCP = r - img2
GCP = g - img2
BCP = b - img2
b,g,r = cv2.split(img) 
maskb,maskg,maskr = cv2.split(img) 
bb,gg,rr = cv2.split(img)
b1,g1,r1 = cv2.split(img)
#blueb,blueg,bluer = cv2.split(img) 
mergedR,mergedG,mergedB = cv2.split(img)
for i in range(height):
     for j in range(width):
         b1[i,j]=0
         g1[i,j]=0
         r1[i,j]=0
         bb[i,j]=0
         gg[i,j]=0
         rr[i,j]=0
         mergedR[i,j]=0
         mergedG[i,j]=0
         mergedB[i,j]=0
for i in range(height):
     for j in range(width):
          if (GCP[i,j] >= 200):
                b1[i,j] = b[i,j]
                g1[i,j] = g[i,j]
                r1[i,j] = r[i,j]
RP = RCP -  cv2.divide(GCP, 2) - cv2.divide(BCP, 2)
count=0
for i in range(height):
     for j in range(width):
         if(RP[i,j]!=0):
             count=count +1
leafarray=np.arange(count)
ii=0
for i in range(height):
     for j in range(width):
         if(RP[i,j]!=0):
             leafarray[ii] = RP[i,j]
             ii=ii+1
maxi=0
x=0
freq = collections.Counter(leafarray)
for (key, value) in freq.items(): 
      #print (key, " -> ", value) 
      if(maxi<value):
          maxi=value
          x = key
print (x, " -> ", maxi) 
print(np.mean(leafarray))
import math
thre=math.floor(np.mean(leafarray))
thre=thre+3
print(thre)
"""
List=     leafarray.tolist()
counter=0
num = leafarray[0]
for i in leafarray:
        curr_frequency = leafarray.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
"""            
for i in range(height):
      for j in range(width):
            if (RP[i,j] > thr):
                   bb[i,j] = b[i,j]
                   gg[i,j] = g[i,j]
                   rr[i,j] = r[i,j]
                   mergedR[i,j] = r[i,j]
                   mergedG[i,j] = g[i,j]
                   mergedB[i,j] = b[i,j]
                   r[i,j]=0
                   g[i,j]=0
                   b[i,j]=0
            if (GCP[i,j]>= 200): 
                  mergedR[i,j] = r[i,j]
                  mergedG[i,j] = g[i,j]
                  mergedB[i,j] = b[i,j]
                  r[i,j]=0
                  g[i,j]=0
                  b[i,j]=0
img1= cv2.merge((b,g,r))
x1,x2,x3= cv2.split(img1)
"""
for i in range(height):
      for j in range(width):
          if(RP[i,j]>thre):
             r[i,j]=255
             g[i,j]=242
             b[i,j]=0
          if(GCP[i,j]>200):  
             r[i,j]=128
             g[i,j]=0
             b[i,j]=0
         # if((r[i,j]>0 and r[i,j]<=5) and (g[i,j]>0 and r[i,j]<=5) and (b[i,j]>0 and b[i,j]<=5)):
          if(x1[i,j]>5 and x2[i,j]>5 and x3[i,j]>5):
             r[i,j]=0
             g[i,j]=255
             b[i,j]=0
  """        
          
img1= cv2.merge((b,g,r))
maskimg = cv2.merge((resr,resg,resb))
greenimg = cv2.merge((b1,g1,r1))                 
redimg = cv2.merge((bb,gg,rr))                   
merimg = cv2.merge((mergedB,mergedG,mergedR))          
cv2.imshow('merimg',merimg)
#cv2.imshow('RP',RP)
#cv2.imshow('BCP',BCP)
#cv2.imshow('GCP',GCP)
cv2.imshow('redimg',redimg)
cv2.imshow('green',greenimg)
cv2.imshow('img1', img1)
#cv2.imshow('res',res)
cv2.imshow('img', img)
#cv2.imshow('img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()