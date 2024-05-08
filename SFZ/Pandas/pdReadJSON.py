import pandas as pd

df = pd.read_json('Pandas/data.js')

print(df.head(10)) 
print(df.info())