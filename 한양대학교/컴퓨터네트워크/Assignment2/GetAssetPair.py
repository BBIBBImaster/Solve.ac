import requests

# Kraken API URL
url = "https://api.kraken.com/0/public/AssetPairs"

# GET 요청으로 거래 가능한 자산 쌍 정보 확인
response = requests.get(url)
asset_pairs_info = response.json()

# 응답 결과 출력
print(asset_pairs_info)
