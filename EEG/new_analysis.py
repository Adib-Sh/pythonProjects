###DO NOT CHANGE ANYTHING HERE###

import os
import glob
import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
#==================================================================================


path = "C://Users//neoad//Documents//GitHub//pythonProjects//EEG//raw_data"
#path = "C://Users//adisha//Downloads//Documents//git//pythonProjects-1//EEG//raw_data"


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
Refi_li = ['be','bp','we']

li1= []
li2= []
li3= []
df1 = df.groupby(['participant','iEvent'])['CorScorePair'].sum().reset_index(name='eScorePair')
eScoreEvent = df.groupby(['participant','iEvent'])['CorScoreEvent'].sum()
eScoreDetail = df.groupby(['participant','iEvent'])['CorScoreDetail'].sum()
df1.insert(3,'eScoreEvent',eScoreEvent.tolist())
df1.insert(4,'eScoreDetail',eScoreDetail.tolist())


ref = df.groupby(['participant','iEvent'])['Refi2'].value_counts()
ref = ref.reset_index(name='RefCount')
refdict ={'be':[],'bp':[],'we':[]}
for partnum in range (1, len(csv_files)+1):
    for eventnum in range (1, 61):
        ref1=ref.query("participant == @partnum")
        ref1=ref1.query("iEvent == @eventnum")
        
        for reftype in Refi_li:
            ref2=ref1.query("Refi2 == @reftype")
            if ref2.empty:
                refdict[reftype].append( np.NaN)
            else:
                refdict[reftype].append(ref2.iloc[0]['RefCount'])

refser = pd.Series(refdict)
for key in Refi_li:
       df1[key+'Count']= refser[key]
df1 = df1.fillna(0)        



#convert df to csv
df1.to_csv( "new_analysis.csv", index=False, encoding='utf-8-sig')

#==================================================================================