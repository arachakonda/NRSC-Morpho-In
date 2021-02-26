import numpy as np
import matplotlib.pyplot as plt
import cv2


img=cv2.imread('bw.png',0)
img2=cv2.imread('fcc.png')
kernel = np.ones((2,2),np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#taking the blurred version of the original image through gaussian filter
#gaussian_opening=cv2.GaussianBlur(opening,(9,9),1.0)
#unsharp_masked_opening=cv2.addWeighted(opening,1.8,gaussian_opening,-0.8,0,opening) 

cv2.imwrite('opened img.png',opening)
opening = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opened img color.png',opening)
#cv2.imwrite('unsharp masked opening.png',unsharp_masked_opening)

cv2.waitKey(0)