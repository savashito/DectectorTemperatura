# Main.py



print "Hola mundo"


url = "http://api.openweathermap.org/data/2.5/forecast?lat=19.43&lon=-99.177&appid=5cdd2e951fbaedb44576f5e53d85fd16"


import requests
r = requests.get(url)
mexJSON =  r.json()
tKelvin = mexJSON["list"][0]['main']['temp']
tCelsius = tKelvin - 273.15
print tCelsius

# print mexJSON["list"][0]['main']['temp']
# _id = '315202'  # id for Eskisehir
# key = '5cdd2e951fbaedb44576f5e53d85fd16'   # api key
# url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=' + _id + '&APPID=' + key   # full url
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon} 
# http://api.openweathermap.org/data/2.5/forecast?lat=19.43&lon=-99.177&appid=5cdd2e951fbaedb44576f5e53d85fd16
# print url
# req = urllib2.Request(url)
# response = urllib2.urlopen(req)
# # the_page = response.read()
# # print the_page.list[0]
# print response
# response = urlopen(url).read().decode('utf-8')
# obj = json.loads(response)
# # name = obj['city']['name']
# print obj
# print name