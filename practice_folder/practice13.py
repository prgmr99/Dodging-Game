# 사전
# 키는 중복될 수 없다.
cabinet= {3:"유재석",100:"김태호"}

# # 사전에서 값을 불어오는 방법 1
# print(cabinet[3])
# print(cabinet[100])

# # 사전에서 값을 불어오는 방법 1
# print(cabinet.get(3))

# print(cabinet[5]) # cabinet 사전에 5라는 키가 없기 때문에 프로그램이 여기서 끝남
# print("hi") # 그래서 hi가 출력되지 않음.

# print(cabinet.get(5)) # 위와 다르게 오류가 발생하지 않고 None 출력한다.
# print("hi") # 그리고 hi도 출력된다.


# # None이 아니라 다른 값을 출력하고 싶다.
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# # 사전 자료 안에 어떤 값이 있는 확인 하는 법
# print(3 in cabinet) # key in 변수 # True
# print(5 in cabinet) # False

cabinet={"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 등장
print(cabinet)
cabinet["C-20"]="조세호" # C-20이라는 키에 "조세호"라는 값을 넣는다. 이미 키가 사용 중이라면 업데이트 된다.
cabinet["A-3"]="김종국"
print(cabinet)

# 간 손님 
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모두 없애기
cabinet.clear()
print(cabinet)