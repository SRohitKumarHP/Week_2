import cv2
img = cv2.imread('T.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gb = cv2.GaussianBlur(gray, (3,3), 0)
mb = cv2.medianBlur(gray, 3)
ret, th = cv2.threshold(mb, 172, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold', th)
cv2.waitKey(0)
cv2.destroyAllWindows()