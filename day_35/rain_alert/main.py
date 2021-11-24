from typing import List, Any
from twilio.rest import Client
import requests
import os

api_key = "5c7bf8bcb5eef4c674e9e994bd27027c"
# api_key_temp = "69f04e4613056b159c2761a9d9e664d2"
url_api_onetime_call = "https://api.openweathermap.org/data/2.5/onecall"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC5bc524185462dc297c503a96996ff8fc'
auth_token = '64d2e2d523901adcf0ffe1ffac42d5f5'

# https://www.latlong.net/
LAT_LODZ = "51.759048"
LON_LODZ = "19.458599"

LAT_WAW = 52.234980
LON_WAW = 21.008490

LAT_VANTA = 60.294410
LON_VANTA = 25.040070

LAT_BB = 49.807621
LON_BB = 19.055840

parameters_onetime_all = {
    "lat": LAT_BB,
    "lon": LON_BB,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

data = requests.get(url_api_onetime_call, params=parameters_onetime_all)
data.raise_for_status()
# print(data.status_code)

weather_data = data.json()
# print(weather_data)

# bring_an_umbrella = [weather_id for weather_id in weather_data['hourly']['weather'][0]['id'] if weather_id < str(800)]
# print(bring_an_umbrella)
# for hourly in weather_data['hourly']:
#     if hourly['weather'][0]['id'] < 800:
#         print(f"Bring an umbrella, id:{hourly['weather'][0]['id']}")

weather_slice = weather_data['hourly'][:12]
# print(weather_slice)
print(weather_data)
will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's ging to rain today. Remember to bring an umbrella.",
        from_='+12184007348',
        to='' # number phone
    )
    print(message.status)
