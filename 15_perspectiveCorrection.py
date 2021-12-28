# 스캔뜬것 처럼 만들어 보자!

import cv2
import numpy as np

from utils import get_four_points

image = cv2.imread('data/images/book1.jpg')

#cv2.imshow("original", image)

# 클릭할때는 시계방향으로 하자! 
# 점 다찍으면 엔터나 스페이스바!
point_src = get_four_points(image)

print(point_src)


# 없는걸 만들수는 없어서 가로세로의 검정 이미지를 만들어준다.
# 변환할 비어있는 이미지를 먼저 하나 만든다.
dst_size = (400, 300, 3)

image_dst = np.zeros(dst_size, np.uint8)

# 이제, 아까했던 14번 파일처럼!
# 이미지 2개가 다 준비되었다.
# 14번 파일을 참고하여, 실습 1번 문제를 해결해보자!

# 힌트, image 의 4개의 점은, 마우스 클릭으로 해결완료!!
# 1. image_dst 의 4개의 점은 여러분들이 구해서 
# 2. 행렬 구하고 
# 3. 변환함수를 통해, 이미지를 가져오세요.

point_dst = np.array([0,0, 300, 0, 300, 400, 0, 400])
point_dst = point_dst.reshape(4,2)

matrix , status = cv2.findHomography(point_src, point_dst)

result = cv2.warpPerspective(image, matrix, (dst_size[1], dst_size[0]))

cv2.imshow('Warp', result)


cv2.waitKey(0)
cv2.destroyAllWindows()