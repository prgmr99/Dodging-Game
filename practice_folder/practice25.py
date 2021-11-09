# 지역변수 & 전역변수

gun=10

# def checkpoint(soldiers):
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers  # 지역 변수 gun은 할당되지도 않았고 초기화도 되지 않았다.
#     print("[함수 내] 남은 총: {0}".format(gun))


def checkpoint_ret(gun,soldiers):
    gun=gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun
print("전체 총: {0}".format(gun))
# checkpoint(2)
gun =checkpoint_ret(gun,2)
print("남은 총: {0}".format(gun))

# 전역변수 사용은 권장되지 않음.

