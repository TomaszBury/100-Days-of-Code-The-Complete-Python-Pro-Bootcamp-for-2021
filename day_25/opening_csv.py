with open("weather_data.csv") as data_file:
    weather_data = data_file.readlines()

for weather in weather_data:
    print(weather)
