#import urllib.request
#opener=urllib.request.build_opener()
#response=opener.open("https://httpbin.org/get")
#print(response.read())

import requests

response=requests.get("https://minfin.com.ua/currency/usd/")
response_text=response.text
response_text=response.text
response_parse=response_text.split("</div>")
print(response_text)
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("₴"):
        for parse_elem_2 in parse_elem_1.split("</div>"):
            if parse_elem_2.startswith("₴") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)
bitcoin_exchange_rate = res_parse_list[0]
print(dollar_exchange_rate)
