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

COLORS = (BLACK, BLUE, GREEN, CYAN, YELLOW, RED, MAGENTA)
iColor = 0

## points
p0, p1 = (80, 50), (200, 100)

winTitle= 'draw lines with left, middle to switch colors'
## mouse event
def mouse(event, x, y, flags, param):
    global p0, p1, iColor, COLORS
    if event == cv2.EVENT_LBUTTONDOWN and flags == 1:
        p0 = x, y
        p1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == 1:
        p1 = x, y
        img[:] = img0
        cv2.line(img, p0, p1, GRAY, 2)
    elif event == cv2.EVENT_LBUTTONUP:
        img[:] = img0
        cv2.line(img, p0, p1, COLORS[iColor], 4)
        img0[:] = img
    elif event == cv2.EVENT_MBUTTONDOWN:
        iColor += 1
        if iColor>6:
            iColor = 0
    cv2.imshow(winTitle, img)

img0 = 240*np.ones((400, 600, 3), np.uint8)
img = img0.copy()
cv2.imshow(winTitle, img)
cv2.setMouseCallback(winTitle, mouse)
