import requests
 
url = "http://server:80/"
 
response = requests.get(url)
print(response.json())