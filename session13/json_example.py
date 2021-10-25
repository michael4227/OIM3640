# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

import urllib.request
import json

APIKEY = 'ce93208cd4f103313fb5e02486627eb8'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?
response_data['main']['temp']