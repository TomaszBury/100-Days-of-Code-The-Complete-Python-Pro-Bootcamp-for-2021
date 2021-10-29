import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
