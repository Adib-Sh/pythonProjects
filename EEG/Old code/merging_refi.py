###DO NOT CHANGE ANYTHING HERE###

import os
import glob
import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
#==================================================================================


path = "D:\\dibs\\your_todays_version\\BehData_correct\\"


# joining files as a list
csv_files = glob.glob(os.path.join(path, "*.csv"))
# sorting the list of the files
csv_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))


  
# loop over the list of csv files
li= []
n = 1
for f in csv_files:

    data = pd.read_table(f, delimiter =";")   # read the csv file
     
    data['participant'] = n                   # inserting the participant num col
    n += 1
    li.append(data)                           # appending all the data gathered in a list
    
# converting the list into a dataframe

df = pd.concat(li, axis=0, ignore_index=True)
df = df.dropna()
    
df = df[['participant','rank','NrmzMeanConfPair','NrmzMeanConfEvent','NrmzMeanConfDetail','Refi']]
Refi_li = ['bpR','bpF','beR','weR']
li1= []
li2= []
li3= []
for item in Refi_li:
    df1 = df.filter(item)
    df1 = df.groupby('rank')['NrmzMeanConfPair'].mean().reset_index(name='NrmzMeanConfPairMean')
    df1['Refi'] = item
    df2 = df.groupby('rank')['NrmzMeanConfEvent'].mean().reset_index(name='NrmzMeanConfEventMean')
    df2['Refi'] = item
    df3 = df.groupby('rank')['NrmzMeanConfDetail'].mean().reset_index(name='NrmzMeanConfDetailMean')
    df3['Refi'] = item
    li1.append(df1)
    li2.append(df2['NrmzMeanConfEventMean'])
    li3.append(df3['NrmzMeanConfDetailMean'])
liList = [li1,li2,li3]
df3 = pd.concat((pd.Series(x) for x in liList), axis=1)  
#df3 = pd.concat(li1, axis=0, ignore_index=True)
#convert df to csv
#df3.to_csv( "merged_refi2.csv", index=False, encoding='utf-8-sig')
'''
df1 = df.groupby(['Refi','rank'])['NrmzMeanConfPair'].mean().reset_index(name='NrmzMeanConfPairMean')
df2 = df.groupby(['Refi','rank'])['NrmzMeanConfPair'].sem().reset_index(name='NrmzMeanConfPairSEM')

x = df1['rank']
y = df1['NrmzMeanConfPairMean']
yerr = df2['NrmzMeanConfPairSEM']
plt.errorbar(x, y, yerr, ecolor= 'green', fmt=None)
'''
#==================================================================================
