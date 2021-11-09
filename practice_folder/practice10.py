# 문자열 포맷

# print("a"+"b") #띄어쓰기 X
# print("a","b") #띄어쓰기 O

# 방법 1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아한다." % "python")
# print("Apple은 %c로 시작해요" %"A")


# # %s로 가능
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" % ("파란","검정"))


# 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","검정"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란","검정"))  #0-0번째, 1-1번째
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","검정"))
# 중괄호 안에 숫자를 넣으면 순서에 맞게 출력된다.


# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.". format(age=20,color="보라"))
# print("나는 {age}살이며, {color}색을 좋아해요.". format(color="보라",age=20))


# 방법 4 (v3.6이상)
age=20
color="흰"
print(f"나는 {age}살이며, {color}색을 좋아해요.")