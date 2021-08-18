import cv2
import numpy as np

img = cv2.imread("Resources/lambo.png")
imgResize = cv2.resize(img, (350, 200))

imgCropped = img[100: 200, 300: 600]
print(img.shape)
print(imgResize.shape)
cv2.imshow("First one", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)