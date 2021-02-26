from scipy import ndimage as nimg
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import inpaint
from skimage.filters import threshold_otsu
import  cv2

image=nimg.imread('satellite img.png',flatten=False,mode='HSV')
image_rgb=nimg.imread('satellite img.png',flatten=False,mode='RGB')



#Sectioning the image for further processing
im_1=image[2000:2500,3000:3500]
imr_1=image_rgb[2000:2500,3000:3500]

#saving the sectioned image
plt.imsave('ORIGINAL IMAGE.png',imr_1)

rows=im_1.shape[1]
columns=im_1.shape[0]


mask1=np.zeros(im_1.shape)
mask2=np.zeros(im_1.shape)



for i in range(rows):
    for j in range(columns):
        v=im_1.item(i,j,2)
        
        if v <=100  :
            mask1.itemset((i,j,0),1)
            mask1.itemset((i,j,1),1)
            mask1.itemset((i,j,2),1)
        if v<=70 :
            mask2.itemset((i,j,0),1)
            mask2.itemset((i,j,1),1)
            mask2.itemset((i,j,2),1)
            
            


plt.imsave('mask1.png',mask1)
plt.imsave('mask2.png',mask2)
mask_f1=cv2.imread('mask1.png',0)
mask_f2=cv2.imread('mask2.png',0)
#masf_f=nimg.median_filter(mask_f,5)
#plt.imshow(masf_f)
#plt.imsave('mask.png',masf_f)
image_result_g1=cv2.inpaint(imr_1,mask_f1,800,cv2.INPAINT_NS)
image_result_g2=cv2.inpaint(imr_1,mask_f2,400,cv2.INPAINT_NS)
kernel = np.ones((2,2),np.uint8)


final_result=cv2.add(image_result_g1,image_result_g2)

final_result2=cv2.morphologyEx(image_result_g2,cv2.MORPH_OPEN,kernel)

plt.imsave('bgr compound image opened.png',final_result2)
plt.imsave('bgr compound image.png',final_result)
plt.imsave('bgr result image fless 800 100 river.png',image_result_g1)
plt.imsave('bgr result image fless 400 70 river.png',image_result_g2)


