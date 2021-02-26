# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:00:12 2017

@author: Ananth
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def padwithones(image,pad_width,iaxis,kwargs):
    image[:pad_width[0]]=255
    image[-pad_width[1]:]=255
    return image

def erosion(image):
    #duplicate array created with padded pixels
    pad_image=np.lib.pad(image,2,padwithones)
    result_image=image
    rows=image.shape[0]
    columns=image.shape[1]
    st=np.array([[1,1,1],[1,1,1],[1,1,1]])
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            matrix=np.array([[pad_image.item(i-1,j-1)*st.item(0),pad_image.item(i-1,j)*st.item(1),pad_image.item(i-1,j+1)*st.item(2)],
                             [pad_image.item(i,j-1)*st.item(3),pad_image.item(i,j)*st.item(4),pad_image.item(i,j+1)*st.item(5)],
                             [pad_image.item(i+1,j-1)*st.item(6),pad_image.item(i+1,j)*st.item(7),pad_image.item(i+1,j+1)*st.item(8)]])
            
            vals=matrix.flatten()
            minval=min(i for i in vals if i>0)
            maxval=max(i for i in vals if i>0)
            #if (np.where(matrix > 245)):
                #new_image.itemset((i,j),np.nanmin(matrix))
            result_image.itemset((i,j),minval) #erosion
        
    
    
    return result_image

def dilation(image):
    #duplicate array created with padded pixels
    pad_image=np.lib.pad(image,2,padwithones)
    result_image=image
    rows=image.shape[0]
    columns=image.shape[1]
    st=np.array([[0,0,0],[0,1,0],[0,0,0]])
    for i in range(1,rows-1):
        for j in range(1,columns-1):
            matrix=np.array([[pad_image.item(i-1,j-1)*st.item(0),pad_image.item(i-1,j)*st.item(1),pad_image.item(i-1,j+1)*st.item(2)],
                             [pad_image.item(i,j-1)*st.item(3),pad_image.item(i,j)*st.item(4),pad_image.item(i,j+1)*st.item(5)],
                             [pad_image.item(i+1,j-1)*st.item(6),pad_image.item(i+1,j)*st.item(7),pad_image.item(i+1,j+1)*st.item(8)]])
            
            vals=matrix.flatten()
            minval=min(i for i in vals if i>0)
            maxval=max(i for i in vals if i>0)
            #if (np.where(matrix > 245)):
                #new_image.itemset((i,j),np.nanmin(matrix))
            result_image.itemset((i,j),maxval) #dilation
    
    
    return result_image

image=cv2.imread('bw.png',0)

#eroded image using padded image
eroded=erosion(image)
dilated_a_erosion=dilation(eroded)#morphological opening of the image

cv2.imshow('eroded image',eroded)
cv2.imshow('eroded after dilation image',dilated_a_erosion)
cv2.imwrite('eroded image with nrke.png',eroded)
cv2.imwrite('eroded after dilation image with nrke.png',dilated_a_erosion)


cv2.waitKey(0)