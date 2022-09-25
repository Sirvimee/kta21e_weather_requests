import requests
import json

url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
info = json.loads(result.text)

print(info['properties']['timeseries'][0]['time'], end = ' ')
print(info['properties']['timeseries'][0]['data']['instant']['details']['air_temperature'], end = '')
print('C')
print(info['properties']['timeseries'][1]['time'], end = ' ')
print(info['properties']['timeseries'][1]['data']['instant']['details']['air_temperature'], end = '')
print('C')
print(info['properties']['timeseries'][2]['time'], end = ' ')
print(info['properties']['timeseries'][2]['data']['instant']['details']['air_temperature'], end = '')
print('C')


