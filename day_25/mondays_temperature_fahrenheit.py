import pandas as pd

data = pd.read_csv("weather_data.csv")
print(f"C:{int(data[data.day == 'Monday'].temp)}\nF:{int(data[data.day == 'Monday'].temp) * 1.8 + 32}")
