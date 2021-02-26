import numpy as np
import scipy
import cv2
import matplotlib

cap=cv2.VideoCapture(0)


ix,iy=-1,-1
h,s,v=[0,0,0]
def get_color_position(event,x,y,flags,param):
    global ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    return
cv2.namedWindow('frame')
cv2.setMouseCallback('frame',get_color_position)

#first capture color through hsv
c_color=False
while(not c_color):
    ret,frame = cap.read() 
    
    if ret == True:
        image=frame
        cv2.imshow('frame',image)  
        if(ix != -1 and iy !=  -1):
            hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
            h=hsv.item(iy,ix,0)
            s=hsv.item(iy,ix,1)
            v=hsv.item(iy,ix,2)
            c_color=True
            break
         
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

#going for mask after the color is obtained
while(True):
    ret,frame = cap.read()
    if ret == True:
        image=frame
        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        l_c=np.array([h-10,s,0])
        u_c=np.array([h+10,255,255])
        mask = cv2.inRange(hsv,l_c,u_c) 
        cv2.imshow('mask',mask)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        

#hsv_val=[h,s,v]
cursor=[iy,ix]
print(cursor)
cap.release()
cv2.destroyAllWindows()
    
    
    