## imports
import cv2 
import numpy as np
import time

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
P0 = (20, 10)
P1 = (100,40)
P2 = (30, 150)
P3 = (50,180)

## draw lines

img = 200*np.ones((200,400,3))
thickness = 2
cv2.line(img, P0, P1, RED, thickness)
cv2.line(img, P2, P1, BLUE, 2*thickness)
cv2.imshow('',img)

## add another line in green
cv2.line(img, P2, P3, GREEN, 4*thickness)
cv2.imshow('',img)

    
