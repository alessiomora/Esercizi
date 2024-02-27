import requests
 
url = "http://server:80/"
# url = "http://20.241.134.170:80/"

response = requests.get(url)
print(response.json())