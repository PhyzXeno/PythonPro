import requests
import re

url = "http://ip4.me"
r = requests.get(url)
result = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",str(r.content))
print("Your IP address is:",result[0])

