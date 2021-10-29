import pandas
data = pandas.read_csv("weather_data.csv")
print(f"{data['temp'].mean():.4f}")

