# 모듈은 내가 쓰려는 파일과 같은 경로에 있거나
# 파이썬 라이브러리에 모여 있는 폴더에 있어야 사용가능하다.

# 지금은 PythonWorkPlace에 같이 있기 때문에 사용가능.

# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# *=NULL이라고 읽음
# from theater_module import *
# # from random import*
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price,price_morning # 전역을 해서 군인에 대한 정보가 필요없을 때
# price(5)
# price_morning(6)

from theater_module import price_soldier as price
price(4) #위의 price와 다르다. price_soldier를 price로 이름바꿔서 사용함.