'''Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님이다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성해라.

조건 1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해진다.
조건 2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 한다.

(출력문 예제)
[0] 1번째 손님 (소요시간:15분)
[ ] 2번째 손님 (소요시간:50분)
[0] 3번째 손님 (소요시간:5분)
...
[ ] 50번째 손님 (소요시간:16분)

총 탑승 승객: 2명'''

# from random import*
# customer=list(range(1,51))
# check="unknown"
# count=0

# for i in customer:
#     customer_time=randint(5,50)
#     driver_time=range(5,16)
#     if customer_time in driver_time:
#         check="O"
#         count+=1
#     else:
#         check=" "
#     print("[{0}] {1}번째 손님 (소요시간: {2}분)".format(check,i,customer_time))

# print("총 탑승 승객: {0}명". format(count))

#------------------------------------------------------------------------

from random import*
cnt=0
for i in range(1,51):
    time=randrange(5,51)
    if 5<= time <= 15:
        print("[0] {0}번째 손님 (소요시간:{1}분)".format(i,time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님 (소요시간:{1}분)".format(i,time))

print("총 탑승 승객: {0}명". format(cnt))