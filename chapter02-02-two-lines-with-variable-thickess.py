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
## define points
p0, p1 = (100, 150), (200, 200)
p2 = (50, 250)
redX, greenX, maxX = 2, 2, 30

def REDtrackbar(x):
    x = max(1, x)
    global greenX, redX
    redX = x
    img[:] = WHITE
    cv2.line(img, p0, p1, RED, redX)
    cv2.line(img, p2, p1, GREEN, greenX)
    cv2.imshow('', img)

def GREENtrackbar(x):
    x = max(1, x)
    global greenX, redX
    greenX = x
    img[:] = WHITE
    cv2.line(img, p0, p1, RED, redX)
    cv2.line(img, p2, p1, GREEN, greenX)
    cv2.imshow('', img)
    
img = np.ones((300, 600, 3), np.uint8)
img[:] = WHITE
cv2.line(img, p0, p1, RED, redX)
cv2.line(img, p2, p1, GREEN, greenX)
cv2.imshow('', img)
cv2.createTrackbar('RED-thickness', '', redX, maxX,  REDtrackbar)
cv2.createTrackbar('GREEN-thickness', '', greenX, maxX, GREENtrackbar)
