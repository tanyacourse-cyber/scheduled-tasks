import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 50.208017,
    "lon": 30.543963,
    "units": "metric",
    "cnt": 4,
    "appid": api_key
}


response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
response_status = response.status_code
weather_data = response.json()
print(response_status)
print(weather_data)

will_rain = False

for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Take an umbrella!")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, remember to bring an ☂️",
        from_="+17405549260",
        to="+380931192277",
    )
    print(message.body)
    print(message.status)
