# import travel.thailand
# trip_to=travel.thailand.ThailandPackage()
# trip_to.detail()

# 주의할 점 import를 사용할 때, import 뒤에는 모듈이나 패키지만 가능하다.
# class나 함수는 import 뒤에 바로 올 수가 없다.

# import travel.thailand.ThailandPackage 에러


# 아래처럼은 사용가능하다.
# from travel.thailand import ThailandPackage
# trip_to=ThailandPackage()
# trip_to.detail()

# from travel import veitnam
# trip_to=veitnam.VeitnamPackage()
# trip_to.detail()

# *을 쓴다는 것은 travel에 있는 모든 것을 가져오겠다는 뜻
# 대신에 문법적으로 공개하려는 범위를 설정해야한다.

from travel import *
# trip_to=vietnam.VietnamPackage()
# # trip_to=thailand.ThailandPackage() 공개를 하지 않았기 때문에 오류발생.
# trip_to=thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # 이 랜덤이라는 모듈이 어느 위치에 있는지 파일 정보를 알려준다.
print(inspect.getfile(thailand))