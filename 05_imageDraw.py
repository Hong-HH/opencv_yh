import cv2
import numpy as np

image = cv2.imread('data/images/mark.jpg')

cv2.imshow('img', image)

# 선 그리기
# 넘파이 어레이 카피하는 법
imageLine = image.copy()
cv2.line(imageLine, (321,179), (400,183), (0,0,255), 3, cv2.LINE_AA)

cv2.imshow('img Line', imageLine)

# 원 그리기
imageCircle = image.copy()
cv2.circle(imageCircle, (350, 200), 150, (255,0,0),3, cv2.LINE_AA)
cv2.imshow("img circle", imageCircle)

# 타원 그리기
imageEllipse = image.copy()
cv2.ellipse(imageEllipse, (360,200), (100,170), 45, 0, 360, (0,255,0),2)
cv2.ellipse(imageEllipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), 2)
cv2.imshow("img elipse", imageEllipse)

# 사각형 그리기
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (208,55),(450,355), (255,0,0),3 )
cv2.imshow("rectangle", imageRectangle)

# 글자 넣기
imageText = image.copy()
cv2.putText(imageText, "Mark Zuckerberg", (205,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('text', imageText)


cv2.waitKey(0)
cv2.destroyAllWindows()