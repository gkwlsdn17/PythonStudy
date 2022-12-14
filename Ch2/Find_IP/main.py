import socket
import requests
import re

# in_addr = socket.gethostbyname(socket.gethostname())
# print(in_addr)

# 가상환경에서도 정확하게 내부 ip 확인


in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print(f'내부 ip: {in_addr.getsockname()[0]}')


# 외부 ip 확인
req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print(f'외부 ip: {out_addr}')