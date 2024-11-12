import time
import urllib.parse
import hashlib
import hmac
import base64
import requests

class Kraken(object):
    api_url = "https://api.kraken.com"

    def get_kraken_signature(self, urlpath, data):
        postdata = urllib.parse.urlencode(data)
        encoded = (str(data['nonce']) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()

        mac = hmac.new(base64.b64decode(self.api_sec), message, hashlib.sha512)
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    def kraken_request(self, uri_path, data):
        headers = {}
        headers['API-Key'] = self.api_key
        headers['API-Sign'] = self.get_kraken_signature(uri_path, data)
        req = requests.post((self.api_url + uri_path), headers=headers, data=data)
        print(f"응답 코드: {req.status_code}")
        return req

    def place_order(self, volume, pair, buy_price, order_type="buy"):
        resp = self.kraken_request('/0/private/AddOrder', {
            "nonce": str(int(1000 * time.time())),
            "ordertype": "limit",
            "type": order_type,
            "volume": volume,
            "pair": pair,
            "price": buy_price
        })
        return resp.json()

    def get_balance(self):
        resp = self.kraken_request('/0/private/Balance', {
            "nonce": str(int(1000 * time.time()))
        })
        return resp.json()


if __name__ == '__main__':
    kr = Kraken()
    response1 = kr.get_balance()
    response2 = kr.place_order(volume="0.01", pair="XBTUSD", buy_price="40000", order_type="sell")
    print(response1)
    print(response2)
