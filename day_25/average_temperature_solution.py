import pandas as pd

data = pd.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
average_temperature = sum(temp_list) / len(temp_list)
print(f"Avr temp:{average_temperature:.4f}")
