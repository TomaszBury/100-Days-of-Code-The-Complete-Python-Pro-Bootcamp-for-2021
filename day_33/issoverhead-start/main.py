import smtplib
import time
import requests
from datetime import datetime

# Your latitude
MY_LAT = 51.759048
# Your longitude
MY_LONG = 19.458599
MY_EMAIL = "erica.schultz54@ethereal.email"
PASSWORD = "AMUEYVnjQHdmDEFUu3"

response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()
data_iss = response_iss.json()

iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
# If the ISS is close to my current position
def is_iss_overhead():
    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True
    return False


# and it is currently dark
def is_it_dar():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()
    data_sun = response_sun.json()
    sunrise = int(data_sun["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_sun["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset < time_now or sunrise > time_now:
        return True
    return False


# Then send me an email to tell me to look up.
while True:
    time.sleep(6)
    if is_iss_overhead() and is_it_dar():
        with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="tomasz.bury@fake_at_fake.uk",
                msg=f"ISS is on horizon."
            )
# BONUS: run the code every 60 seconds.
