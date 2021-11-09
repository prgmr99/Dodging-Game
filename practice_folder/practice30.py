# with

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))


# profile.pickle","rb" 을 열어서 -> profile_file라는 변수에 저장을 해두고
# -> profile_file 내용을 pickle이 로드를 통해서 불러와서 출력을 한 것.
# .close()는 with 문에서는 필요없음. 자동으로 해줌.

with open("study.txt","w",encoding="utf8") as study_files:
    study_files.write("파이썬을 열심히 공부하고 있다. 이거다!")

with open("study.txt","r",encoding="utf8") as study_files:
    print(study_files.read())