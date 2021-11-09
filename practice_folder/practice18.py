# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# for waiting_no in [0,1,2,3,4]:   #range(5): 0,1,2,3,4 이용 가능
#     print("대기번호: {0}".format(waiting_no))


# starbucks=["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비됐습니다.".format(customer))

# customer="토르"
# index=5
# while index >=1:
#     print("{0}, 커피가 준비됐습니다. {1}번 남았어요". format(customer,index))
#     index-=1
#     if index==0:
#         print("커피 버렸다.")

# customer="아이언맨"
# index=1
# while True:
#     print("{0}, 커피가 준비됐습니다. 호출 {1}회".format(customer,index))
#     index+=1

customer="토르"
person="Unknown"

while person != customer:
    print("{0}, 커피가 준비됐습니다.".format(customer))
    person=input("이름이 어떻게 되세요? ")