# 이번엔 반대로 침식

import cv2

image = cv2.imread('data/images/truth.png')

cv2.imshow('original', image)

# 이미지 침식 : erode

erodeSize = 6

# 밑에 shape에 따라 모양이 다르게 확장된다/ cross 예쁘다...
element = cv2.getStructuringElement(cv2.MORPH_RECT, (2*erodeSize, 2*erodeSize))

imageErode = cv2.erode(image, element)

cv2.imshow('erode', imageErode)

cv2.waitKey(0)
cv2.destroyAllWindows()



# 이 방법을 사용하면 작은 잡티같은것을 침식시켜서 없앤 뒤 확장시켜서 잡티가 사라진 원래 사진으로 되돌릴 수 있다.
