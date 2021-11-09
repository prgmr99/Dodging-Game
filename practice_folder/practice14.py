# 튜플 -> 내용 변경/추가 할 수 없다. (리스트와 다름) 대신 속도가 빠름

menu=("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") 오류발생

name="김종국"
age=20
hobby="코딩"
print(name,age,hobby)

name,age,hobby="김종국",20,"코딩"
print(name,age,hobby)