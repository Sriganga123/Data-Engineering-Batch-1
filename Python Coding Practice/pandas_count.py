# Count values in Pandas dataframe
import numpy as np
import pandas as pd

# create dataframe with missing values
NaN = np.nan
dataframe = pd.DataFrame({'Name': ['Shobhit', 'Vaibhav',
                                   'Vimal', 'Sourabh',
                                   'Rahul', 'Shobhit'],
                          'Physics': [11, 12, 13, 14, NaN, 11],
                          'Chemistry': [10, 14, NaN, 18, 20, 10],
                          'Math': [13, 10, 15, NaN, NaN, 13]})
print(dataframe)
print("Count with respect to column:")
print(dataframe.count())

#count all the values with respect to row give axis=0 or axis='columns'
print("Count with respect to row:")
print(dataframe.count(axis=1))

#count null values in our dataframe.
#count of individual columns count of null values
print("Count of null values of individual columns")
print(dataframe.isnull().sum())

# count of total null values present in our dataframe
print("Count of total null values")
print(dataframe.isnull().sum().sum())

#count no of students whose physics marks are greater than 11.
print("Count of students with physics marks greater than 11 is->",
      dataframe[dataframe['Physics'] > 11]['Name'].count())
print(dataframe[dataframe['Physics']>11])

#Count of students whose physics marks are greater than 10,
# chemistry marks are greater than 11 and math marks are greater than 9.
print("Count of students is ->",dataframe[(dataframe["Physics"]>10)&(dataframe["Chemistry"]>11)&
                                          (dataframe["Math"]>9)]['Name'].count())

print(dataframe[(dataframe['Physics'] > 10) &
                (dataframe['Chemistry'] > 11) &
                (dataframe['Math'] > 9)])

