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
COLORS= (BLACK, BLUE, CYAN, GREEN, YELLOW, RED, MAGENTA)
## define points
p0, p1 = (50, 150), (100, 50)
p2 = (50, 250)

color= COLORS[0]
thickness= 2
def ColorTrackbar(x):
    global color, COLORS, thickness
    color = COLORS[x]
    img[:] = WHITE
    cv2.line(img, p0, p1, color, thickness)
    cv2.imshow('', img)

def ThicknessTrackbar(x):
    x = max(1, x)
    global color, COLORS, thickness
    thickness = x
    img[:] = WHITE
    cv2.line(img, p0, p1, color, thickness)
    cv2.imshow('', img)
    
img = np.ones((300, 600, 3), np.uint8)
img[:] = WHITE
cv2.line(img, p0, p1, color, thickness)

cv2.imshow('', img)
cv2.createTrackbar('thickness', '', 2, 30,  ThicknessTrackbar)
cv2.createTrackbar('color', '', 0,6, ColorTrackbar)
