import cv2
import numpy as np 

## draw red using the left button, clear using the middle
# adapted from the code by <Abhishek Kumar>
drawing = False # true if mouse is pressed
pt1_x , pt1_y = None , None

windowTitle= 'ESC to exit'
def line_drawing(event,x,y,flags,param):
    global pt1_x,pt1_y,drawing, img

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        pt1_x,pt1_y=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
            pt1_x,pt1_y=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.line(img,(pt1_x,pt1_y),(x,y),color=(0,0,255),thickness=1)
    elif event== cv2.EVENT_MBUTTONDOWN:
        img= 250*np.ones((400, 400, 3), 'uint8')
        cv2.imshow(windowTitle,img)

img = np.zeros((512,512,3), np.uint8)
img =  250*np.ones((400, 400, 3), 'uint8')

#img = cv2.imread('blank-page-01.png')
cv2.namedWindow(windowTitle)
cv2.setMouseCallback(windowTitle,line_drawing)

while(1):
    cv2.imshow(windowTitle,img)
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()
        break

