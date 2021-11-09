'''Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있다.
보고서는 항상 아래와 같은 형태로 출력되어야 한다.

- X 주차 주간보고 - 
부서:
이름:
업무 요약:

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건: 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만든다.'''

# for i in range(1,51):
#     report_file=open("{0}주차.txt",'w',encoding="utf8".format(i))
#     report_file.write("- {0}주차 주간보고 -\n".format(i))
#     report_file.write("부서: \n")
#     report_file.write("이름: \n")
#     report_file.write("업무 요약: \n")
#     report_file.close()


# for i in range(1,51):
#     report_file=open("{0}주자.txt",'r',encoding="utf8".format(i))
#     print(report_file.read())
#     report_file.close()

# 파일들이 저장이 안되어있나봐. 파일을 읽으려는데 찾을 수가 없다고 해.

# report_file=open("1주차.txt",'w',encoding="utf8")
# report_file.write("- 1주차 주간보고 -")
# report_file.write("부서: ")
# report_file.write("이름: ")
# report_file.write("업무 요약: ")
# report_file.close()

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as report_file:    # 분리해서 하는 생각을 못했다.
        report_file.write("- {0}주차 주간보고 -".format(i))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")
