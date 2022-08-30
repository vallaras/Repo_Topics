import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
conn = sqlite3.connect(r"C:\Users\ELCOT\PycharmProjects\trining\tkemployee\vallarasu.db")
sql='select * from employee01'
query = pd.read_sql_query(sql, conn)
df = pd.DataFrame(query)
print(df)
df.plot(x = 'name', y = 'total',kind ='bar')
plt.show()

