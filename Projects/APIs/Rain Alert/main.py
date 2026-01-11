#For weather alert
import requests
from twilio.rest import Client

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "Accound ID generated in twilio app"
auth_token = "Your auth token generated in twilio app"

weather_params = {
    "appid" : "Weather application ID",
    "lat" : 13.082680,
    "lon" : 80.270721,
    "cnt" : 4
}

response = requests.get(OWN_ENDPOINT, params=weather_params, timeout=5)
response.raise_for_status()
data = response.json()
# print(data)
# print(data['cod'])
next_4_timestamp = data["list"]
will_rain = False
for item in next_4_timestamp:
    weather_id = item["weather"][0]["id"]
    if weather_id <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Its gonna rain today. Carry umbrella",
        from_="Twilio number",
        to="Your phone number",
    )
    print(message.status)

    