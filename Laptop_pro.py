import pandas as pd

import re

df=pd.read_csv("laptops.csv",encoding=('ISO-8859-1'))

regex = 'IPS Panel Retina Display 2560x1600'

result = df[df.ScreenResolution.str.match(regex)]

col_match = ["Company","Product","ScreenResolution"]

new_t = result[col_match]
print(new_t)