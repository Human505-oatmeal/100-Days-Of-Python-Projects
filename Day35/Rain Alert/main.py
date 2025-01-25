import requests
from twilio.rest import Client

api_key = "REDACTED"
weather_url = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "REDACTED"
auth_token = "REDACTED"

params = {
    "lat": 30.267153,
    "lon": -97.743057,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=weather_url, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for weather in weather_data['list']:
    condition_code = weather['weather'][0]['id']
    if int(condition_code) <= 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+REDACTED',
        body='It\'s gonna rain today, bring an umbrella! ☔',
        to='+REDACTED'
    )
    print(message.status)
