import requests

api_key = "5c7bf8bcb5eef4c674e9e994bd27027c"
api_key_temp = "69f04e4613056b159c2761a9d9e664d2"

url_api_onetime_call = "https://api.openweathermap.org/data/2.5/onecall"

# https://www.latlong.net/
LAT_LODZ = "51.759048"
LON_LODZ = "19.458599"

parameters_onetime_all = {
    "lat": LAT_LODZ,
    "lon": LON_LODZ,
    "appid": api_key_temp,
}

data = requests.get(url_api_onetime_call, params=parameters_onetime_all)

print(data.status_code)

print(data.json())
