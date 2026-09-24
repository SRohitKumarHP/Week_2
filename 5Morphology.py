import cv2
import numpy as np

img = cv2.imread('2.jpg', 0)

kernel = np.ones((3,3), np.uint8)

eroded  = cv2.erode(img, kernel, iterations=1)
dilated = cv2.dilate(img, kernel, iterations=1)

opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('eroded.png', eroded)
cv2.imwrite('dilated.png', dilated)
cv2.imwrite('opened.png', opened)
cv2.imwrite('closed.png', closed)