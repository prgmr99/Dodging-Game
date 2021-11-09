# 예외처리
try:
    print("나누기 전용 계산기입니다.")
    nums=[]
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0]/nums[1]))
    print("{0}/{1}={2}".format(nums[0],nums[1],nums[2]))

except ValueError:
    print("에러가 발생했다 이놈아!!!!!")

except ZeroDivisionError as err:
    print(err)

except: #IndexError도 사용가능하지요 #나머지 모든 에러 여기서 처리 가능
    print("알 수 없는 에러가 발생하였습니다.")

