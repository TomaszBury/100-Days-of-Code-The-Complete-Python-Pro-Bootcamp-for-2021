import pandas as pd

data = pd.read_csv("./data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data["Primary Fur Color"].value_counts())

unique_fur_color = data["Primary Fur Color"].value_counts()

print(type(unique_fur_color))

squirrel_count = pd.DataFrame(unique_fur_color)
print(squirrel_count)
print(type(squirrel_count))
squirrel_count.to_csv("./data/squirrel_count.csv")
