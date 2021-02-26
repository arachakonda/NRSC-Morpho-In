import numpy as np
import matplotlib.pyplot as plt
import cv2

def padwithones(image,pad_width,iaxis,kwargs):
    image[:pad_width[0]]=1
    image[-pad_width[1]:]=1
    return image

def erosion(image):
    #duplicate array ccreated with padded pixels
    new_image=image
    rows=image.shape[0]
    columns=image.shape[1]
    st=np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    for i in range(1,rows-2):
        for j in range(1,columns-2):
            matrix=np.array([[image.item(i-2,j-2)*st.item(0),image.item(i-2,j-1)*st.item(1),image.item(i-2,j)*st.item(2),image.item(i-2,j+1)*st.item(3),image.item(i-2,j+2)*st.item(4)]
                             ,[image.item(i-1,j-2)*st.item(5),image.item(i-1,j-1)*st.item(6),image.item(i-1,j)*st.item(7),image.item(i-1,j+1)*st.item(8),image.item(i-1,j+2)*st.item(9)]
                             ,[image.item(i,j-2)*st.item(10),image.item(i,j-1)*st.item(11),image.item(i,j)*st.item(12),image.item(i,j+1)*st.item(13),image.item(i,j+2)*st.item(14)]
                             ,[image.item(i+1,j-2)*st.item(15),image.item(i+1,j-1)*st.item(16),image.item(i+1,j)*st.item(17),image.item(i+1,j+1)*st.item(18),image.item(i+1,j+2)*st.item(19)]
                             ,[image.item(i+2,j-2)*st.item(20),image.item(i+2,j-1)*st.item(21),image.item(i+2,j)*st.item(22),image.item(i+2,j+1)*st.item(23),image.item(i+2,j+2)*st.item(24)]])
    
            #matrix=np.array([[image.item(i-1,j-1),image.item(i-1,j)],[image.item(i,j-1),image.item(i,j)]])
            print(matrix)
            #print(np.min(np.nonzero(matrix)))
            vals=matrix.flatten()
            minval=min(i for i in vals if i>0)
            if (np.where(matrix > 245)):
                new_image.itemset((i,j),minval)
    
    return new_image
            
image=cv2.imread('bw.png',cv2.IMREAD_GRAYSCALE)

eroded=erosion(image)
cv2.imshow('eroded image',eroded)
cv2.imwrite('eroded image 2 by 2.png',eroded)
cv2.waitKey(0)