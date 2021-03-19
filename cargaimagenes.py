import cv2 
import numpy as np
#cargar imagen a color
IRGB=cv2.imread("009.jpg")
print(IRGB)
print(IRGB.shape)
print("lineas agregadas en mai")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)
cv2.imwrite('004GS.jpg',IGS)
