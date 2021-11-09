# 가변인자

# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")  # end=" " 프린특가 끝날 때, 줄 바꿈을 하지않고 " "로 끝낸다는 말
#     print(lang1,lang2,lang3,lang4,lang5)

# profile("유재소",20,"python","java","c++","c#","c")
# profile("김태흎", 25, "Kotlin","swift"," "," "," ")


def profile(name,age,*language):
    print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=' ')
    print() # 줄바꿈

profile("유재소",20,"python","java","c++","c#","c","javascript")
profile("김태흎", 25, "Kotlin","swift")