import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

# img[:,300:] = 255, 0 , 0
cv2.line(img,(50, 70), (img.shape[1], img.shape[0]),(0,255, 0),3 )
cv2.rectangle(img,(0,0), (300, 400), (0,0,255),3)
cv2.circle(img, (200, 200), 50, (255,0,255), 3)
cv2.putText(img, "Vui hoc", (300, 300), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,150,0), 1)
cv2.imshow("Image",img)

cv2.waitKey(0)

