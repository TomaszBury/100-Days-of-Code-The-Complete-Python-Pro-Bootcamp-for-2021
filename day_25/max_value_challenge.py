import pandas as pd

data = pd.read_csv("weather_data.csv")
print(f"List of temperatures:\n{data['temp']}")
print(f'Max temperature:{data["temp"].max():.2f}')
print(f"\n\n{data.condition}")
