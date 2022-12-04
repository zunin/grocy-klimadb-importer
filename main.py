import pandas as pd
import os
from typing import NamedTuple

df = pd.read_excel(io='klimadbv1.xlsx', sheet_name='Ra_500food')

class Product(NamedTuple):
    Index: int
    ID_Ra_500prod: str
    Navn: str
    Name: str
    Unit: str
    Agriculture: str
    iLUC: str
    Packaging: str
    Transport: str
    Retail: str
    Comments: str
    ID_food: str
    ID_pack: str
    ID_retail: str


rows: list[Product] = list(df.itertuples(name='Product'))
print(rows[0].Navn)

#for row in rows:
#    print(row)
#    print(Product(**dict(filter(lambda kv: not kv[0].startswith("_"), row._asdict().items()))))
#
#
#    print(5*"=")
