class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        # super().__init__()  
        Unit.__init__(self)
        Flyable.__init__(self)

# 두 개 이상의 부모클래스를 다중상속 받을 때는
# super를 사용하면 뒤의 부모클래스는 호출이 되지 않는 문제 발생
# 따라서 따로따로 명시해주면 좋다. 

dropship=FlyableUnit()