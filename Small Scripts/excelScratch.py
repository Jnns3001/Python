import pandas as pd
file = "D:/Beladung_MLF BMH"

df = pd.read_excel(file+".xlsx")
print(df.to_string())

f = open(file+'.txt', 'w', encoding='utf-8')
f.write(df.to_string())
f.close()

f = open(file+'.json', 'w', encoding='utf-8')
f.write(df.to_json())
f.close()
