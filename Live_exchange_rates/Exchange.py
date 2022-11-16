import urllib3
import json

url = "https://api.exchangerate.host/latest/"
http = urllib3.PoolManager()

response = http.request('GET', url)
