import cv2
# from scipy.signal import wiener

img = cv2.imread('T.jpg')
resized = cv2.resize(img, (548,720))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

rev, th = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)

bf = cv2.bilateralFilter(th, 11, 50, 80)

# blur = cv2.GaussianBlur(th, (1,1), 0)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 2))
# thin = cv2.erode(bf, kernel, iterations=100)

cv2.imshow('I', resized)
cv2.imshow('bf', bf)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('T2.jpg', bf)