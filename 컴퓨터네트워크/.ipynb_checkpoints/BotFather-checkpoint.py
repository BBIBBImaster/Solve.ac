import requests
import telepot
import urllib3
from telepot.loop import MessageLoop
import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# SSL 인증서 경고 무시
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Etherscan API Endpoint 및 API 키
url = 'https://api.etherscan.io/api'
api_key = 'CFPZJXMWMR9PCM9B1RAB2BJUMXIYEQMJDE'

# 텔레그램 API 토큰 및 사용자 chat_id
TOKEN = '7600258423:AAHuzj4NUzmg2IMAN3MY0hiqSwJosTWxGf0'
CHAT_ID = '5880689318' 

# 봇 객체 생성
bot = telepot.Bot(TOKEN)

# 이전 가스 가격 및 사용 비율을 저장할 변수
previous_fast_gas_price = None
previous_gas_used_ratio = None

# 가스 통계 정보를 가져오는 함수
def get_gas_statistics():
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

            # 가스 가격 정보 반환
            return fast_gas_price, gas_used_ratio
        else:
            return None, None
    else:
        return None, None

# 가스 정보를 텔레그램으로 전송하는 함수
def send_gas_statistics():
    global previous_fast_gas_price, previous_gas_used_ratio

    fast_gas_price, gas_used_ratio = get_gas_statistics()

    if fast_gas_price is not None and gas_used_ratio is not None:
        # 변화량 계산
        if previous_fast_gas_price is not None:
            price_change = fast_gas_price - previous_fast_gas_price
            ratio_change = gas_used_ratio - previous_gas_used_ratio
        else:
            price_change = 0
            ratio_change = 0

        # 메시지 생성
        message = (f"FastGasPrice: {fast_gas_price:.2f} Gwei, "
                   f"GasUsedRatio: {gas_used_ratio:.2f}%, "
                   f"Change: {price_change:.2f}")

        # 결과를 텔레그램으로 전송
        bot.sendMessage(CHAT_ID, message)

        # 현재 값을 이전 값으로 저장
        previous_fast_gas_price = fast_gas_price
        previous_gas_used_ratio = gas_used_ratio

    else:
        bot.sendMessage(CHAT_ID, "Etherscan API로부터 데이터를 가져올 수 없습니다.")

# "/restart" 명령어로 변화량을 초기화하는 함수
def reset_change():
    global previous_fast_gas_price, previous_gas_used_ratio
    previous_fast_gas_price = None
    previous_gas_used_ratio = None
    bot.sendMessage(CHAT_ID, "Change has been reset to 0. Tracking will restart.")

# 메시지를 처리하는 함수
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        text = msg['text']

        # 사용자가 "/gas" 명령어를 입력하면 즉시 가스 통계를 제공
        if text == '/gas':
            send_gas_statistics()
        # "/restart" 명령어로 주기적 업데이트 재시작 및 변화량 초기화
        elif text == '/restart':
            reset_change()
        # 기타 명령어 처리
        else:
            bot.sendMessage(chat_id, "지원되는 명령어는 '/gas' 및 '/restart'입니다.")

# 2분마다 가스 통계를 자동으로 전송하는 스케줄러
scheduler = BackgroundScheduler()
scheduler.add_job(send_gas_statistics, 'interval', minutes=2, next_run_time=datetime.now())
scheduler.start()

# 메시지 루프 시작
MessageLoop(bot, handle).run_as_thread()
print('Listening...')

# 프로그램이 계속 실행되도록 유지
while True:
    time.sleep(10)
