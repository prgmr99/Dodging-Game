python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자인지 확인하는 함수 -> 맞다면 True / 틀리면 False
print(len(python))

print(python.replace("Python","Java"))

print(python.replace("Amazing", "trash")) #replace를 해도 일시적으로 변경할 뿐 영구적으로 바뀌지 않는다.

print(python)


index = python.index("n")
print(index)

index = python.index("n", index+1) # 첫 번째 n의 다음 n부터 찾는다.
print(index)

print(python.find("n")) # 원하는 값이 포함되어 있지 않으면 -1 출력.
print(python.find("Java")) #-1
# print(python.index("Java")) #error

print(python.count("n")) # 원하는 문자열이 몇 개 있는지 카운트해준다.
