import numpy as np
import pandas as pd

#Create a dataframe using np.random.randn function with 5 rows and 4 columns, and performs various operations using pandas library

lst=np.random.rand(5,4)
df=pd.DataFrame(lst,index=['r1','r2','r3','r4','r5'],columns=['c1','c2','c3','c4'])
print(df.head())
x=df['c1'].value_counts()
print("different value in c1:")
print(x)
print("\nSUM OF VALUES OF C1:",df['c1'].sum())
