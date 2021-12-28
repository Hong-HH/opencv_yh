import cv2

image = cv2.imread('data/images/opening.png')

cv2.imshow('original', image)

openingSize = 3

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (2*openingSize, 2*openingSize))

# 침식하고 다시 확장하는것을 오픈이라 한다. iteration은 반복이다.
imageOpened = cv2.morphologyEx(image, cv2.MORPH_OPEN, element, iterations=5)

cv2.imshow('open', imageOpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
