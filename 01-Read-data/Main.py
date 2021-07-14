import pandas as pd
import numpy as np


# membaca file csv
dataku = pd.read_csv('dataku.csv')
print(dataku.tail())


# mengclone atau membuat file csv baru dari data csv yang sudah ada

dataku.to_csv('dataCsvBaru', index=False)

dataBaru = pd.read_csv('dataCsvBaru')
print(dataBaru.head())



# mengclone dari csv ke xlss

# dataku.to_excel('dataExcel', index=False)

