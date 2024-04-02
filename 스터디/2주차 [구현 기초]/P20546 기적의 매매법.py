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

def TIMMING (cash, stock_price) :
    timing_stock_cnt = 0
    for i in range(13) :
        print("")

    # 현재 소유한 주식의 가격이 3일째 상승한다면, 전량 매도한다. 
    # 3일 연속 가격이 전일 대비 하락하는 주식은 다음날 무조건 가격이 상승한다고 가정한다. 
    # 따라서 이러한 경향이 나타나면 즉시 주식을 전량 매수한다.



cash = int(input())
stock_price = list(map(int, input().split()))
print(BNP(cash, stock_price))
print(TIMMING(cash, stock_price))


