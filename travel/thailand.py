

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원 ")


if __name__=="__main__":  # 내부에서 사용하는 건지 외부에서 사용하는 건지 확인할 수 있다.
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요.")
    trip_to=ThailandPackage()
    trip_to.detail()

else:
    print("Thailand 외부에서 모듈 호출")