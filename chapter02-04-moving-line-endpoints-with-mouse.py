
import cv2
import numpy as np
color1 = (200, 10, 100)
thickness= 3
p0, p1 = (100, 30), (400, 90)
winTitle= "click left/right buttons to move end points"
def mouse(event, x, y, flags, param):
    global p0, p1
    
    if event == cv2.EVENT_LBUTTONDOWN:
        p0 = x, y
    elif event== cv2.EVENT_RBUTTONDOWN:
        p1 = x,y
    
    img[:] = 240
    cv2.line(img, p0, p1, color1, thickness)
    cv2.imshow(winTitle, img)
        
img = 240*np.ones((300, 600, 3), np.uint8)
cv2.line(img, p0, p1, color1, thickness)
cv2.imshow(winTitle, img)
cv2.setMouseCallback(winTitle, mouse)

