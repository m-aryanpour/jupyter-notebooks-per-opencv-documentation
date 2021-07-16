import cv2
import numpy as np

## define main colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE  = (255,0,0)
GREEN = (0,255,0)
RED   = (0,0,255)
CYAN  = (255,255,0)
MAGENTA = (255,0,255)
YELLOW = (0,255,255)
GRAY   = (100, 100, 100)

COLORS = (WHITE, BLUE, GREEN, CYAN, YELLOW, RED, MAGENTA)
iColor = 0
winTitle = 'draw polyline '

points = []
## drawing function
def drawPolyline(x):
    global p0, p1, winText
    d = cv2.getTrackbarPos('thickness', winTitle)
    d = -1 if d==0 else d
    i = cv2.getTrackbarPos('color', winTitle)
    color = COLORS[i]
    img[:] = img0
    try:
        cv2.polylines(img, np.array([points]), True, color, d)
    except:
        pass
    winText = f'color={color}, thickness={d}'
    cv2.putText(img,winText,(1, 20), cv2.FONT_HERSHEY_SIMPLEX,0.4, YELLOW, 1)
    cv2.imshow(winTitle, img)
## mouse events
def mouse(event, x, y, flags, param):
    global pts
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        drawPolyline(0)

## main

img0 = np.ones((400, 600, 3), np.uint8)
img = img0.copy()
cv2.imshow(winTitle, img)
cv2.setMouseCallback(winTitle, mouse)
cv2.createTrackbar('color', winTitle, 0, 6, drawPolyline)
cv2.createTrackbar('thickness', winTitle, 0, 10, drawPolyline)



           
