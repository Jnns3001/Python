import pandas as pd

a = [1, 7, 4]
myDataSeries = pd.Series(a, index=["x", "y", "z"])


print(myDataSeries)
print(myDataSeries["x"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
myvar2 = pd.Series(calories, index = ["day1", "day2"])