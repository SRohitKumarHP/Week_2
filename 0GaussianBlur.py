import cv2
img = cv2.imread('2.jpg')
gb0 = cv2.GaussianBlur(img,(3,3),0)
gb = cv2.GaussianBlur(img,(3,3),10)
cv2.imshow('I', img)
cv2.imshow('Gaussian Blur0', gb0)
cv2.imshow('Gaussian Blur1', gb)
cv2.waitKey(0)
cv2.destroyAllWindows()