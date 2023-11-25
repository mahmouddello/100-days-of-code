import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())
print("-" * 25)

squirrel_count = pd.DataFrame({
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [2473, 392, 103]
})
print(squirrel_count)
squirrel_count_csv = squirrel_count.to_csv("squirrel_count.csv")
