import cv2

image = cv2.imread('data/images/sample.jpg')

print(image.shape)

cv2.imshow('original', image)

# 회전시킬 이미지를 만들기 위한 정보 셋팅 (x, y) 좌표
center = (image.shape[1] / 2 , image.shape[0] /2)
rotationAngle = 30
# 이건 확대 축소 비율
scaleFactor = 1

# 회전시킬 수 있는 행렬을 먼저 얻어와야 한다.
matrix = cv2.getRotationMatrix2D(center, rotationAngle, scaleFactor)
print(matrix)

# 회전 시킬 수 있는 행렬을 얻어왔으니, 이 행렬로 변환하라는 함수 호출 m은 변환시켜줄 행렬
result = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))

cv2.imshow('rotation', result)


cv2.waitKey(0)
cv2.destroyAllWindows()
