import cv2

image = cv2.imread('data/images/closing.png')

cv2.imshow('original', image)

closeSize = 3
# 컨볼루션 할때처럼 홀수로하는것이 좋다 
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*closeSize, 2*closeSize))

imageClose = cv2.morphologyEx(image,cv2.MORPH_CLOSE, element, iterations=3)

cv2.imshow('close', imageClose)

cv2.waitKey(0)
cv2.destroyAllWindows()