# # 파일입출력
# score_file=open("score.txt","w",encoding="utf8") # utf8을 써야 한글 정보를 읽을 수 있다. 쓰는 습관을 들이면 좋다.
# print("수학: 0",file=score_file)     # w - 쓰기/덮어쓰기
# print("영어: 50",file=score_file)
# score_file.close()

# score_file=open("score.txt",'a',encoding="utf8") # a - 내용추가
# score_file.write("과학: 80" )
# score_file.write("\n코딩: 100" )  # print에는 자동으로 줄바꿈이 있지만 write 함수에는 그런 거 없다. 그래서 줄바꿈 넣어줌
# score_file.close()


# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.read()) # read() 파일에 있는 모든 내용을 다 읽어와서 출력해줌.
# score_file.close()

# score_file=open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end='')  # 한 줄씩만 읽어와서 커서를 다음 줄로 이동시킴.
# print(score_file.readline(),end='')  # 한 줄씩만 읽어와서 커서를 다음 줄로 이동시킴.
# print(score_file.readline(),end='')  # 한 줄씩만 읽어와서 커서를 다음 줄로 이동시킴.
# print(score_file.readline(),end='')  # 한 줄씩만 읽어와서 커서를 다음 줄로 이동시킴.
# score_file.close()

# 파일에 몇 줄이 있는 지 모를때
# score_file=open("score.txt","r",encoding="utf8")
# while True: 
#     line=score_file.readline()
#     if not line:
#         break   # 마지막에는 값이 없기 때문에 if문 들어와서 break
#     print(line)

# score_file.close()

score_file=open("score.txt","r",encoding="utf8")
lines=score_file.readlines() # list형태로 저장
for line in lines:
    print(line,end="")

score_file.close()