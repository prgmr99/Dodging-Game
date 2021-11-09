# name="마린"
# hp=40
# damage=5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# tank_name="탱크"
# tank_hp=100
# tank_damage=50

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))


# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)


class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))

# marine1=Unit("마린",40,5)
# marine2=Unit("마린",40,5)
# tank1=Unit("탱크",140,25)

# # __init__ 생성자이다. 객체가 만들어질 때 자동으로 호출된다.
# # marine1,tank..처럼 클래스로부터 만들어진 녀석들 -> 객체
# # marine과 tank는 Unit클래스의 인스턴스

# wraith1=Unit("레이스",80,5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name,wraith1.damage)) # 멤버 변수 사용법 클래스 외부에서

# wraith2=Unit("빼앗은 레이스",80,5)
# wraith2.clocking=True # 외부에서 객체에 추가로 변수를 만들어서 사용할 수 있다.

# if wraith2.clocking ==True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# # wraith1에는 clocking 변수가 없어서 오류발생.


class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage

    def attack(self,lotation):
        print("{0}:{1} 방향으로 적군을 공격합니다.[공격력{2}]".format(self.name,lotation,self.damage))

    def damaged(self,damage):
        print("{0}:{1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{0}:현재 체력은 {1}입니다.".format(self.name,self.hp))

        if self.hp<=0:
            print("{0}: 파괴되었습니다.".format(self.name))

firebat1=AttackUnit("파이어뱃",50,16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)
