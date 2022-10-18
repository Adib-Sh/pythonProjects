###DO NOT CHANGE ANYTHING HERE###

import os
import glob
import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
#==================================================================================


path = "C://Users//adisha//Downloads//Documents//git//pythonProjects-1//EEG//raw_data"


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
    
df = df[['participant','iEvent','CorScorePair','CorScoreEvent','CorScoreDetail','Refi2']]
Refi_li = ['bpR','bpF','beR','weR']

#for i in range(0,len(csv_files)):
li1= []
li2= []
li3= []
df1 = df.groupby(['participant','iEvent'])['CorScorePair'].sum().reset_index(name='eScorePair')
eScoreEvent = df.groupby(['participant','iEvent'])['CorScoreEvent'].sum()
eScoreDetail = df.groupby(['participant','iEvent'])['CorScoreDetail'].sum()
df1.insert(3,'eScoreEvent',eScoreEvent.tolist())
df1.insert(4,'eScoreDetail',eScoreDetail.tolist())


#weScorePair = df.groupby(['participant','iEvent','Refi2'])['CorScoreEvent'].sum()

ref = df.groupby(['participant','iEvent'])['Refi2'].value_counts()
ref
#ref = ref.reset_index(name='RefCount')
#ref= ref.sort_values(by=['Refi2']).groupby(['participant','iEvent'])
'''

Z






'''

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
