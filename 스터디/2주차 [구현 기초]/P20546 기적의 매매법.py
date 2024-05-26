import sys
input = sys.stdin.readline

def BNP (cash, stock_price) :
    bnp_stock_cnt = 0
    for i in range(13) :
        # 남은 현금으로 주식을 살 수 있다면,
        if cash // stock_price[i] >= 1 :
            # 살 수 있는 만큼
            bnp_stock_cnt += cash // stock_price[i]
            # 산다.
            cash -= stock_price[i] * bnp_stock_cnt

    return bnp_stock_cnt * stock_price[-1] + cash

def TIMING (cash, stock_price) :
    timing_stock_cnt = 0
    for i in range(10) :
        # 3일 연속 상승한다면,
        if stock_price[i] < stock_price[i+1] < stock_price[i+2] :
            # 4일차(i+3) 전량 매도
            print(i, "전량 매도")
        # 3일 연속 하락한다면,
        if stock_price[i] > stock_price[i+1] > stock_price[i+2] :
            # 4일차(i+3) 전량 매수
            print(i, "전량 매수")

    return timing_stock_cnt * stock_price[-1] + cash
        

cash = int(input())
stock_price = list(map(int, input().split()))

# 확인용
print(BNP(cash, stock_price))
print(TIMING(cash, stock_price))

if BNP(cash, stock_price) > TIMING(cash, stock_price) :
    print("BNP")
elif BNP(cash, stock_price) < TIMING(cash, stock_price) :
    print("TIMING")
else :
    print("SAMESAME")


