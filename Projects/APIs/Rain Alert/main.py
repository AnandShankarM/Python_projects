#For weather alert
import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "appid" : "5018aa3770580e54e5132fa53e4fa895",
    "lat" : 12.971599,
    "lon" : 77.594566,
    "cnt" : 4
}


response = requests.get(OWN_ENDPOINT, params=weather_params, timeout=5)
response.raise_for_status()
data = response.json()
print(data)
# print(data['cod'])
next_4_timestamp = data["list"]
will_rain = False
for item in next_4_timestamp:
    weather_id = item["weather"][0]["id"]
    if weather_id <= 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
    