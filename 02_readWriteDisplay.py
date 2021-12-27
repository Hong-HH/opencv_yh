import cv2
import numpy as np

img_file = 'data/images/sample.jpg'

# opencv 로 이미지 열기, 디폴트로 되어있지만 굳이 썼다 (cv2.IMREAD_COLOR) - 칼라이미지(BGR)
image =cv2.imread(img_file, cv2.IMREAD_COLOR)

# 이미지가 정상인지 체크하는 코드
if image is None :
    print('이미지 파일을 열 수 없습니다.')
else :
    print(image.shape)

# opencv 에서는, 이미지를 BGR로 읽어옵니다. 
# 따라서 불러온 이미지를 그레이스케일로 변경할 수 있습니다.
# cvt 는 컨벌트의 약자

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# "내용" 은 창의 이름으로 입력된다. 
cv2.imshow("color", image)
cv2.imshow("gray scale", gray_image)

# 위의 imshow 함수는 화면에 표시하는 함수인데, 실행되었다가 바로 종료된다.
# 왜냐하면, cpu가 imshow를 실행하고, 아래로 내려가 아래의 라인을 실행하는데
# 아래 라인은 아무것도 없어서 바로 프로그램이 종료되었다.

# 따라서 우리 눈으로 확인하기 위해서는
# cpu의 코드실행을 잠시 멈추게 해야한다. 특이하게도 0 은 내가 키보드키를 누르기 전까지 계속 멈춘다.


cv2.waitKey(0)
cv2.destroyAllWindows()

