'''Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''
#brainstorming
#리스트에 다 저장하고 리스트의 크기를 매물 개수로 하면 될까?

# class House:
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         self.location=location
#         self.house_type=house_type
#         self.deal_type=deal_type
#         self.price=price
#         self.completion_year=completion_year

#     def show_detail(self,location,house_type,deal_type,price,completion_year):
#         if (deal_type=="월세"):
#             print("{0} {1} {2} {3} {4}년".format(location,house_type,deal_type,price,completion_year))
#         else:
#             print("{0} {1} {2} {3}억 {4}년".format(location,house_type,deal_type,price,completion_year))



# class house1(House):
#     def __init__(self):
#         House.__init__(self,"강남","아파트","매매",10,2010)

# class house2(House):
#     def __init__(self):
#         House.__init__(self,"마포","오피스텔","전세",5,2007)

# class house3(House):
#     def __init__(self):
#         House.__init__(self,"송파","빌라","월세","500/50",2000)

# h1=House("강남","아파트","매매",10,2010)
# h2=House("마포","오피스텔","전세",5,2007)
# h3=House("송파","빌라","월세","500/50",2000)

# house_list=[]
# house_list.append(h1)
# house_list.append(h2)
# house_list.append(h3)

# print("총 {0}대의 매물이 있습니다.".format(len(house_list)))

# h1.show_detail("강남","아파트","매매",10,2010)
# h2.show_detail("마포","오피스텔","전세",5,2007)
# h3.show_detail("송파","빌라","월세","500/50",2000)

# 파이썬 메서드의 첫 번째 인자로 항상 인스턴스가 전달된다. self필요!
# 즉 House라는 클래스를 생성하고
# house1=House()라는 객체를 생성하면
# house1.location이런 식으로 사용하는 것.

class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year

    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)


houses=[]
house1=House("강남","아파트","매매","10억","2010년")
house2=House("마포","오피스텔","전세","5억","2007년")
house3=House("송파","빌라","월세","500/50","2000")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()