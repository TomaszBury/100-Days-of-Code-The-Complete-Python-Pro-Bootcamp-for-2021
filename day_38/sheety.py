from datetime import datetime

import requests

sheet_endpoint = "https://api.sheety.co/6ed30aa04f21710d833b8b543a03f91c/workoutTracking/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": "karamba",
        "duration": "60",
        "calories": "karamba_2"
    }
    }


sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

print(sheet_response.text)
