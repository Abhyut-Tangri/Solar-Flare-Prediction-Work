import pandas as pd
import numpy as np

df=pd.read_csv('coverted_data.csv')
print(df.keys())

values_to_replace=[99,999.9,9999,9999999.0,999,999.0,9.999,99.99,999.99,999999.99,99999.99,99999,99.9,9999,9.9999]
#search and replace numbers like 9999.9 9.9 and 99.9, etc
#in future versions make sure that inplace is not used 
names=df.keys()
for name in names:
    df[name].replace(values_to_replace,np.nan,inplace=True )
    

df.to_csv('clean_data.csv')

#print(df)



