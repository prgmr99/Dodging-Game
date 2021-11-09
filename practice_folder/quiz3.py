"""Quiz 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1: http:// 부분은 제외 => naver.com
규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3: 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + '!'로 구성

예) 생성된 비밀번호: nav51!"""

# site="http://naver.com"
# e_count=site.count('e')
# len_site=len(site[7:-4]) # .com, .net 등 3자리에 한정됌. .co.kr하면 틀린다.
# first_three=site[7:10]
# print("생성된 비밀번호: "+first_three+str(len_site)+str(e_count)+"!")

# 해설
url="http://naver.com"
my_str=url.replace("http://","") # 규칙1
my_str=my_str[:my_str.index(".")] # 규칙2

password=my_str[:3]+str(len(my_str))+str(my_str.count('e'))+'!'
print("{0}의 비밀번호는 {1}입니다.". format(url,password))
