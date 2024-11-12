require 'net/http'
require 'uri'
require 'openssl'
require 'base64'
require 'time'
require 'json'

class Kraken
  API_URL = "https://api.kraken.com"

  def get_kraken_signature(urlpath, data)
    postdata = URI.encode_www_form(data)
    nonce = data['nonce']
    encoded = nonce + postdata

    digest = OpenSSL::Digest::SHA256.new
    message = urlpath + digest.digest(encoded)

    mac = OpenSSL::HMAC.digest(OpenSSL::Digest.new('sha512'), Base64.decode64(API_SEC), message)
    Base64.strict_encode64(mac)
  end

  def kraken_request(uri_path, data)
    url = URI.parse(API_URL + uri_path)
    http = Net::HTTP.new(url.host, url.port)
    http.use_ssl = true

    request = Net::HTTP::Post.new(url)
    request['API-Key'] = API_KEY
    request['API-Sign'] = get_kraken_signature(uri_path, data)
    request.set_form_data(data)

    response = http.request(request)
    puts response.code
    JSON.parse(response.body)
  end

  def place_order(volume, pair, buy_price, order_type = "buy")
    kraken_request('/0/private/AddOrder', {
      "nonce" => (Time.now.to_f * 1000).to_i.to_s,
      "ordertype" => "limit",
      "type" => order_type,
      "volume" => volume,
      "pair" => pair,
      "price" => buy_price
    })
  end

  def get_balance
    kraken_request('/0/private/Balance', {
      "nonce" => (Time.now.to_f * 1000).to_i.to_s
    })
  end
end

if __FILE__ == $0
  kr = Kraken.new
  response1 = kr.get_balance
  response2 = kr.place_order("0.01", "XBTUSD", "40000", "sell")

  puts response1
  puts response2
end
