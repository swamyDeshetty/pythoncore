import pandas as pd
a=pd.read_csv('pandas/data.csv')
df=a.dropna(inplace=True)
print(a)
print(a.to_string()) # to string is used to print the entire dataframe..

import pandas as pd
df=pd.read_csv('pandas/marks.csv')
print(df)

#removing the empty cells or nulls
df=pd.read_csv('pandas/data.csv')
new_data=df.fillna(20,inplace=True) #The data don't have the nulls thats'y it is showing the none
print(new_data)

#removing the duplicates
df=pd.read_csv('pandas/data.csv')
new_data=df.drop_duplicates(inplace=True) #The data dont have the duplicates so it is showing the none
print(new_data) 
