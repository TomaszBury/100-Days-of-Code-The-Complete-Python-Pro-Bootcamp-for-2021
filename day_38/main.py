# Application ID
APP_ID = "0194e188"
# Application Keys
API_KEY = "b0e8fbf1f3a1163a1630539d31be328a"
import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "200"
HEIGHT_CM = "110"
AGE = 69




exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6ed30aa04f21710d833b8b543a03f91c/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)