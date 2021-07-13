## imports
import cv2 
import numpy as np
import time
## image class 
class imageApp:
    
    def __init__(self,imgFile,Name='image'): 
        self.imgFile = imgFile
        self.name    = Name
        self.img     = cv2.imread(imgFile)
        
    def window(self):
        cv2.imshow(self.name, self.img)

    def run(self):
        key = 'a'
        self.window()
        while (key != ord('q')):
            key = cv2.waitKey(0)
            print("key= %d. Press 'q' to quit" %key)
        cv2.destroyAllWindows()


## using image class
imageFile1 = 'cable-01.jpg'
img1 = imageApp(imageFile1, Name= 'cable')

        

    
