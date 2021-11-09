animal="강아지"
name="연탄이"
age=4
hobby="산책"
is_adult=age>=3

'''이렇게
하면
여러 문장이
주석처리
됩니다.'''

print("우리 집 " + animal+ " 이름은 "+name)
#print(name+"는 "+ str(age)+"이고,"+hobby+"을 좋아한다.")
print(name,"는 ", str(age),"이고,",hobby,"을 좋아한다.")

print(name+"는 어른일까?" + str(is_adult))

# ctrl+/ 누르면 주석처리/해제 가능하다.