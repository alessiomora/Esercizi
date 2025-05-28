import requests
import time 

url = "http://server:80/"
# url = "http://0.0.0.0:80/"

time.sleep(5)
response = requests.get(url)
print(response.json())