import pandas as pd
import numpy as np
from pandas.core.indexes.base import Index


# membaca file csv
dataku = pd.read_csv('dataku.csv')
print(dataku.tail())


# mengclone atau membuat file csv baru dari data csv yang sudah ada

dataku.to_csv('dataCsvBaru', index=False)

dataBaru = pd.read_csv('dataCsvBaru')
print(dataBaru.head())



# mengclone dari csv ke xlss

# dataku.to_excel('dataExcel', index=False)

dataku.to_excel('dataExel.xlsx', index=False, sheet_name="halaman 1")


# membaca file exel

data1 = pd.read_excel('dataExel.xlsx')

print(data1)



from sqlalchemy import create_engine

mesin = create_engine('sqlite:///:memory:')

dataku.to_sql('dataSql', con=mesin)

pd.read_sql('dataSql', con=mesin)