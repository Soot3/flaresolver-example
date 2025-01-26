import requests
import random

proxy_list = [
    '185.150.85.170',
    '45.154.194.148',
    '104.244.83.140',
    '58.97.241.46',
    '103.250.82.245',
    '83.229.13.167',
]

proxy_ip = random.choice(proxy_list)

proxies = {
   'http': f'http://{proxy_ip}',
   'https': f'https://{proxy_ip}',
}

payload = {
        "cmd": "request.get",
        "url": "https://www.datanearme.co/",
        "maxTimeout": 60000
}

response = requests.post(url, headers=headers, json=data, proxies=proxies)
print("Status Code:", response.status_code)
