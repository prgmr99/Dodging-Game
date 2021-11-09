# 표준입출력


# print("python","java",sep=",",end="?")
# print("무엇이 더 재밌을까요?")
# 지금까지는 end부분이 무조건 줄바꿈하도록 되어있었는데
# ?로 바꾸면서 한 줄에 두 개의 print문이 출력되었다.


# import sys
# print("python","java",file=sys.stdout) # 표준출력으로 출력되는 것.
# print("python","java",file=sys.stderr) # 표준에러로 출력되는 것.

# 시험 성적
# scores={"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(4),str(score).rjust(4),sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호: "+str(num).zfill(3))

answer=input("아무 값이나 입력하세요: ")   #항상 문자열 자료형으로만 입력받는다. int로 변환가능.
print("입력하신 값은 "+ answer+"입니다.")  #자료형은 문자열이다.
