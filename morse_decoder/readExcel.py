import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataFile = "PYTHON\morse_decoder\charset.xlsx"

df = pd.read_excel(dataFile)

print(df.head())