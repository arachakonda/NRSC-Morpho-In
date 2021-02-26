from scipy import ndimage as nimg
import scipy
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2
from skimage.restoration import inpaint

img= nimg.imread('satellite img.png',flatten=False,mode='RGB')
mask=np.zeros(img.shape[:-1])
size=img.shape
rows=int(size[1])
columns=int(size[0])
for i in range(2000,2200):
    for j in range(2000,2200):
         b=img.item(i,j,0)
         g=img.item(i,j,1)
         r=img.item(i,j,2)
         
         if ((b+g+r)/3) == 0:
            mask.itemset((i,j),255)


image_result = inpaint.inpaint_biharmonic(img, mask,multichannel=True)





