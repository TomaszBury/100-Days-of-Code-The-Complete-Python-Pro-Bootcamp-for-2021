from typing import List, Any

import requests

api_key = "5c7bf8bcb5eef4c674e9e994bd27027c"
# api_key_temp = "69f04e4613056b159c2761a9d9e664d2"

url_api_onetime_call = "https://api.openweathermap.org/data/2.5/onecall"

# https://www.latlong.net/
LAT_LODZ = "51.759048"
LON_LODZ = "19.458599"

LAT_WAW = 52.234980
LON_WAW = 21.008490

LAT_VANTA = 60.294410
LON_VANTA = 25.040070


parameters_onetime_all = {
    "lat": LAT_VANTA,
    "lon": LON_VANTA,
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
print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
