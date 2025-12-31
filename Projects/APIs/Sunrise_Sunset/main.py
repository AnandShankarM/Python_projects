import requests

MY_LAT = 12.971599
MY_LONG = 77.594566
parameters = {
    "lat" :  MY_LAT,
    "lng" : MY_LONG
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, timeout=5)
response.raise_for_status()
data = response.json()
print(data)