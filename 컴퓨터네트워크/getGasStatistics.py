import requests
import telepot
import urllib3
from telepot.loop import MessageLoop
import time

# SSL 인증서 경고 무시
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Etherscan API Endpoint 및 API 키


# 봇 객체 생성
bot = telepot.Bot(TOKEN)

# 이전 가스 가격 및 가스 사용 비율 저장 변수
previous_fast_gas_price = None
previous_gas_used_ratio = None

def get_gas_statistics():
    global previous_fast_gas_price, previous_gas_used_ratio

    # Etherscan API로부터 가스 가격 정보 가져오기
    params = {
        'module': 'gastracker',
        'action': 'gasoracle',
        'apikey': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        if data['status'] == '1' and data['message'] == 'OK':
            fast_gas_price = float(data['result']['FastGasPrice'])
            gas_used_ratio = float(data['result']['gasUsedRatio'].split(',')[0])

            # 이전 값과 비교하여 변화량 계산
            if previous_fast_gas_price is not None:
                gas_price_change = fast_gas_price - previous_fast_gas_price
                gas_used_ratio_change = gas_used_ratio - previous_gas_used_ratio

                # 메시지 전송
                message = (f"FastGasPrice: {fast_gas_price:.2f}, GasUsedRatio: {gas_used_ratio:.2f}, "
                           f"Change: {gas_price_change:.2f}")
                bot.sendMessage(CHAT_ID, message)
            else:
                # 처음에는 변화량을 0으로 출력
                message = (f"FastGasPrice: {fast_gas_price:.2f}, GasUsedRatio: {gas_used_ratio:.2f}, "
                           "Change: 0")
                bot.sendMessage(CHAT_ID, message)

            # 현재 값을 이전 값으로 저장
            previous_fast_gas_price = fast_gas_price
            previous_gas_used_ratio = gas_used_ratio

        else:
            print(f"Error: {data['message']}")
    else:
        print(f"HTTP Error: {response.status_code}")

# 주기적으로 Etherscan에서 데이터를 가져오는 함수
def check_gas_statistics_periodically():
    while True:
        get_gas_statistics()
        time.sleep(120)  # 2분에 한 번씩 업데이트

# 메시지를 처리하는 함수
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(f"Received message: {msg}")  # 수신한 메시지 출력 (디버깅용)

    # 사용자가 보낸 텍스트 메시지를 그대로 다시 보냄 (에코)
    if content_type == 'text':
        bot.sendMessage(chat_id, f"Echo: {msg['text']}")

# 메시지 루프 시작
MessageLoop(bot, handle).run_as_thread()
print('Listening...')

# 주기적으로 가스 통계를 가져오고 텔레그램으로 전송
check_gas_statistics_periodically()
