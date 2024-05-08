import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dragons.xlsx")
df.dropna(inplace=True)

res_df = df.sort_values(by = "fish ammount", ascending=False)
print(res_df[["name", "fish ammount"]])