'''Quiz) 표준 체중을 구하는 프로그램을 작성하시오

*표준 체중: 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자: 키(m) x 키(m) x 22
여자: 키(m) x 키(m) x 21

조건 1: 표준 체중은 별도의 함수 내에서 계산
        * 함수명: std_weight
        * 전달값: 키(height), 성별(gender)
조건 2: 표준 체중은 소수점 둘째자리까지 표시

출력 예제
키 175cm 남자의 표준 체중은 67.38kg입니다.'''

# height=int(input("키 입력: "))
# gender=input("성별 입력: ")

# def std_weight(height, gender):
#     if gender=="남자":
#         return round((height/100) * (height/100) *22,2)  # 밑에 해설처럼 새로운 변수에 대입하는 것이 편하다.
#     elif gender=="여자":
#         return round((height/100) * (height/100) *21,2)
#     else:
#         return "error"

# print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height,gender,std_weight(height,gender)))

#---------------------------------------------------------------------

def std_weight(height, gender):   # 키 m 단위로 받을게.
    if gender =="남자":
        return height*height*22
    else:
        return height*height*21

height =175
gender="남자"
weight=round(std_weight(height/100,gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.". format(height,gender,weight))