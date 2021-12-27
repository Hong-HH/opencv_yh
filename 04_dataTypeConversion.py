import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg')

scalingFactor = 1/255.0

# 0~255로 되어있는 이미지를 0~1 사이의 실수로 정규화

source = source * scalingFactor

print(source)

# 반대로, 실수로 되어있는 것을, 다시 0~255로 만드는 방법
# 즉, 다시 이미지 배열로 만드는 방법

source = source * 255
print(source) 
# 위의 코드는 결과가 실수이므로, 이미지 배열이 아니다.
# 따라서 다시 이미지 배열로 만드려면, 데이터 타입을 변경해줘야 한다.
# 변경하는 방법 2개

# 1. np.uint8(source)
# 2. source.astype('uint8')
print(np.uint8(source))
print(source.astype('uint8'))

source = source.astype('uint8')


