import pandas as pd

df = pd.read_csv("Pandas\dirtydata.csv")

new_df = df.dropna()

x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])
df.dropna(subset=["Date"], inplace=True)

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    #df.loc[x, "Duration"] = 120
    df.drop(x, inplace=True)

df.drop_duplicates(inplace=True)

print(df.to_string())
