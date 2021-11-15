import requests
from datetime import datetime
MY_LAT = 53.531441
MY_LONG = 11.302060
response = requests.get(url="http://api.open-notify.org/iss-now.json")

response.raise_for_status()

# if response.status_code == 404:
#     raise Exception("Thtat resource does not exist.")
# elif response.status_code == :
#     raise Exception("Bas response from ISS API")
#
#     print("Error")

print(response.text)

data = response.json()
latitude = response.json()["iss_position"]["latitude"]
longitude = response.json()["iss_position"]["longitude"]
print(data)

print(f"latitude:{latitude}, longitude:{longitude}")

# https://www.latlong.net/
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data_sun = response_sun.json()
sunrise = data_sun["results"]["sunrise"]
sunset = data_sun["results"]["sunset"]
print(f"sunrise:{sunrise}, sunset:{sunset}")

time_now = datetime.now()
print(time_now)
