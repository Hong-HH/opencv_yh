# 한국말로 문지방이라는 뜻으로 넘어갈거냐 안넘어갈거냐
# 특정 숫자(색)을 잡아두고 두개중에 하나로 처리하는 것이다.
# 기준점을 잡고 그보다 아래는 무슨색, 그보다 위는 무슨색으로 정하는 것이다.

import cv2

image = cv2.imread('data/images/truth.png')

# 구분값을 먼저 설정
thresh = 120
# 위의 특정 값보다 큰 값들은 모두 255로 변경
maxValue = 255

cv2.imshow('Original', image)

# 쓰레숄딩 적용된 이미지 만들기(두번째 dst가 넘파이 어레이다.)
th, dst = cv2.threshold(image, thresh, maxValue, cv2.THRESH_BINARY)

cv2.imshow("thresholded image", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
