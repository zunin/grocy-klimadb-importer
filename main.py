import pandas as pd
import os

df = pd.read_excel(io='klimadbv1.xlsx', sheet_name='Ra_500food')
print(df.head(5))  # print first 5 rows of the dataframe
