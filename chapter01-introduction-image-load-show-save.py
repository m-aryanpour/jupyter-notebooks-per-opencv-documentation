## imports
from matplotlib import pyplot as plt
import numpy as np
import cv2

## Load and show an image
img = cv2.imread('fuji-mountain-001.jpg')
img2 = img[:,:,::-1] # supposed to convert BGR to RGB
plt.title('not realistic colors')
plt.imshow(img);
plt.pause(5)
plt.close()

img3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img3)
plt.xticks([]); plt.yticks([]) # comment out to add the graph ticks
plt.title('realistic colors')
plt.pause(5)
plt.close()

## convert to gray
gray_img = 255-cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # invert to the true shades
plt.title('gray image')
plt.imshow(gray_img,cmap='Greys');
plt.pause(5)
plt.close()

## save image to a file
cv2.imwrite('fuji-mountain-001-gray.jpg',255-gray_img);
