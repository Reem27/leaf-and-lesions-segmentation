# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:01:02 2021

@author: x16
"""
import cv2

import matplotlib.pyplot as plt
#846 #589  #1647
import	numpy  as  np
img  =	cv2.imread("C:/Users/x16/Desktop/related to dataset/FiltersandSegmentation/Watershed/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/train/dataset2/DSCN1875.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
mask =	np.zeros(img.shape[:2],np.uint8)
bgdModel =  np.zeros((1,65),np.float64)
fgdModel =  np.zeros((1,65),np.float64)

#rect =	(112,112,461,150)
#rect =	(20,40,461,200) # whiteboard images (5,5,460,250)
#rect =	(5,60,461,250)# complicated background C1P3E2 (20,40,380,170), (5,60,461,200), C1P3H2(15,55,461,200), C1P4H2(20,60,461,200), C1P7H2(0,30,461,200), C1P7E2(0,30,461,200), 
#C1P6H2(0,30,461,200),C1P2E2 (5,20,461,200), C1P2H2 (5,30,461,250) 
#DSC_4065 (10,40,420,270), DSC_4044 (10,60,470,270), DSC_4071 (5,28,350,205)or(5,30,350,200), DSC_4043 (4,60,460,230), rect = DSC_4080(14,60,460,230), DSC_4058(15,60,470,230), 
#DSC_4086(55,70,490,250), DSC_4060(10,60,470,250), C1P8E2(0,30,461,200), C1P9H2(0,30,461,200), C1P9E2(0,30,461,200)
rect=(0,8,512,380)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2  =  np.where((mask==2)|(mask==0),0,1).astype('uint8')
img  =	img*mask2[:,:,np.newaxis]

plt.subplot(121),  plt.imshow(img)
plt.title("grabcut"), plt.xticks([]),	plt.yticks([])
plt.subplot(122),
plt.imshow(cv2.cvtColor(cv2.imread("C:/Users/x16/Desktop/related to dataset/FiltersandSegmentation/Watershed/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/train/dataset2/DSCN1875.jpg"),
cv2.COLOR_BGR2RGB))
plt.title("original"),	plt.xticks([]),	plt.yticks([])
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.imshow('img',img2)
cv2.imwrite("C:/Users/x16/Desktop/related to dataset/FiltersandSegmentation/Watershed/python_for_image_processing_APEER-master/python_for_image_processing_APEER-master/images/train/dataset2/maskedDSCN1875.jpg",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()