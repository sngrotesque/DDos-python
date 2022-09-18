import requests
import random
import time
import os
import sys

def timer():
    s = time.time()
    
    for x in range(300000):
        n = random.randint(4096, 8192)
        b = os.urandom(n)
        len(b)
    e = time.time() - s
    
    return e

# url = 'http://fanick.top:8888/'
# proxy = {
#     'http':  'http://157.100.12.138:999',
#     'https': 'http://157.100.12.138:999'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
# }

# res = requests.get(url, headers = headers, proxies = proxy)
# print(res.text)







