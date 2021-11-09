# 함수 & 전달값과 반환값


def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 함수는 정의만 되는 거지 호출하기 전까지는 실행되지 않는다.


# open_account()

def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.". format(balance+money))
    return balance+money


def withdraw(balance,money): # 출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))


def withdraw_night(balance,money):
    commission=100 # 수수료 100원
    return commission, balance-money-commission # 튜플 형식으로 보내줌.


balance=0 # 잔액
balance=deposit(balance,1000)
# balance=withdraw(balance,500)
commission,balance=withdraw_night(balance,500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.". format(commission,balance)) 