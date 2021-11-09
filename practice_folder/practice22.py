# 기본값

# def profile(name,age,main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name,age,main_lang))

# profile("염승준",23,"C")
# profile("염승군",29,"pyhton")

# 같은 학교, 같은 학년, 같은 반, 같은 수업

def profile(name,age=17,main_lang="python"):  # 17로 초기화함 = 기본값!
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name,age,main_lang))


profile("유재석")
profile("김재석")
