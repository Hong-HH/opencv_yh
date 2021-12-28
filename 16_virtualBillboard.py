import cv2
import numpy as np
from utils import get_four_points

image = cv2.imread('data/images/first-image.jpg')

cv2.imshow('original', image)
print(image.shape)

# 1. 이 이미지를 변환하기 위한 점 4개 구하기
point_original = np.array([0, 0, 600, 0 , 600, 477, 0, 477], dtype=float)
point_original = point_original.reshape(4,2)

# 2. 타임 스퀘어의 이미지에 매칭할 점의 좌표를 구합니다.
image_dst = cv2.imread('data/images/times-square.jpg')

cv2.imshow('dst', image_dst)


point_dst = get_four_points(image_dst)

print(point_dst)

# 3. 위의 두개 이미지간의 매칭할 두 점들을 모두 찾았으니,  변환 행렬을 얻어옵니다.
matrix , status = cv2.findHomography(point_original, point_dst)

# 4. image를 변환시킵니다.

temp = cv2.warpPerspective(image, matrix, (image_dst.shape[1], image_dst.shape[0]))

# 5. 변환된 이미지를 화면에 보여줍니다.
cv2.imshow('temp', temp)

# 6. 타임스퀘어 이미지에, 변환된 이미지 합성
# fill Poly 는 다각형으로 채워라, fill컴백스폴리는 튀어나오게 채워라

# 6-1. 타임스퀘어 이미지의 바꿀 부분을, 0으로 셋팅한다!
#      바꿀 영역은 이미, point_dst에 들어있다.
# 이 함수는 이미지 자체를 바꾼다.
cv2.fillConvexPoly(image_dst, point_dst.astype(int), 0)

cv2.imshow('Image to 0' , image_dst)

# 6-2. 두개의 이미지를 더하면, 합성이 된다.
result = temp + image_dst

cv2.imshow('result', result)



cv2.waitKey(0)
cv2.destroyAllWindows()
