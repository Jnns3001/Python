import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DATA_FILE = "PYTHON\morse_decoder\charset.xlsx"

# Create a Pandas Dataframe
# (read the Excel data with Pandas)
df = pd.read_excel(DATA_FILE)

# print the first five rows
print(df.head())
print(pd.read_excel(DATA_FILE))