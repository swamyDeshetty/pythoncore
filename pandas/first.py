#pandas description:
# 1)pandas is a software library written in python that is used for the dataanalysis and datamanipulation
# 2)pandas mainly works with the tabular data 
# 3)pandas mostused datastructures are series and dataframe
# 4)series is a similar to a single column and dataframe is a similar to sheet with rows and columns..
# There are types of data structures in the pandas
#  1)series      -> 1D
#  2)Dataframe   -> 2D
#  3)panel       -> 3D

#Dataset:
# Data which is in the form of tabel is called the dataset 
#  pandas uses the  dataset to analyze or to manipulate the data
# Using the pandas we can easily anaylize or manipulate the large amount of data

#series:
import pandas as pd
a=[4,5,3,1,8,0]
x=pd.Series(a)
print(x)

a=['swamy','satwika','Manusha','Gouthami']
x=pd.Series(a)
print(x)

#we can aslo specify with the indexes..
a=[1,2,3]

b=pd.Series(a,index=['x','y','z'])
print(b)

import pandas as pd

x={'name':'swamy','age':22,'Role':'pythondeveloper'}

y=pd.Series(x)
print(y)

#pandas
x={
    'name':['swamy','shiva','prasad'],
    'Age':[22,25,26]
}

new=pd.DataFrame(x,index=['x','y','z']) #we can also add the indexes for the pandas
print(new)


y={
    'name':['harish','suhansh','chotu'],
    'age':[30,2,4]
}

x=pd.DataFrame(y)
print(x)

x={
    'name':['Jadeja','Dhoni','Iyer'],
    'age':[34,41,28]
}
y=pd.DataFrame(x)
print(y)
print(y.loc[0])


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 