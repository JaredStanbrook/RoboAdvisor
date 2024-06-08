import requests

url = "https://www.asx.com.au/markets/company/CBA"

headers = {"Content-Type":"text","Host":"www.asx.com.au","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0","Connection":"keep-alive"}

r = requests.get(url,headers)

print(r.content)