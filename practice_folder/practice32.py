#상속
#다중상속(두개 이상의 부모클래스를 상속받는다.)

#일반유닛
class Unit:    # 부모클래스
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
    
    def move(self,location):
        print("[지상 유닛 이동]")
        print("{0}:{1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location,self.speed))

#공격유닛
class AttackUnit(Unit):  #자식클래스
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed)
        self.damage=damage

    def attack(self,location):
        print("{0}:{1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name,location,self.damage))


class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed=flying_speed

    def fly(self,name,location):
        print("{0}:{1}방향으로 날아갑니다.[속도{2}]".format(name,location,self.flying_speed))


class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #지상speed 0
        Flyable.__init__(self,flying_speed) 

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)


# firebat1=AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# valkyrie=FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

# vulture=AttackUnit("벌쳐",80,10,20)

# battlecruiser=FlyableAttackUnit("배틀크루저",500,25,3)

# vulture.move("11시")
# #battlecruiser.fly(battlecruiser.name,"9시")
# battlecruiser.move("9시") # move 재정의한 move가 호출됌.



# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # pass # 일단 pass 오류는 발생하지 않는다.
        # Unit.__init__(self,name,hp,0)  방법 1
        super().__init__(name,hp,0)  # 방법 2 super를 통해서 init을 하면 self는 뺀다.
        self.location=location

supply_depot=BuildingUnit("서플라이 디폿",500,"7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()