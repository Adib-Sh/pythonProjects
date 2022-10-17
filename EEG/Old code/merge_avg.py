###DO NOT CHANGE ANYTHING HERE###

import os
import glob
import pandas as pd
from sklearn import preprocessing
import numpy as np

#==================================================================================


path = "C:\\Users\\neoad\\Downloads\\dibs\\dibs\\your_todays_version\\BehData_correct\\"


# joining files as a list
csv_files = glob.glob(os.path.join(path, "*.csv"))
# sorting the list of the files
csv_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))


  
# loop over the list of csv files
li= []
n = 1
for f in csv_files:

    data = pd.read_table(f, delimiter =";")   # read the csv file

    data = data[data["type"] == 'fixation'] 
    #data = data.dropna()
    data['eNrmzMeanConfPair'] = data['eNrmzMeanConfPair'].str.split('.')
    data['eNrmzMeanConfEvent'] = data['eNrmzMeanConfEvent'].str.split('.')
    data['eNrmzMeanConfDetail'] = data['eNrmzMeanConfDetail'].str.split('.')
    for i, row in data.iterrows():
        x_array = np.array([data.eNrmzMeanConfPair.loc[i]])
        normalized_arr = preprocessing.normalize(x_array)
        mean = np.mean(normalized_arr[0]).item()
        data.at[i,'N_eNrmzMeanConfPair'] = mean
        
        x_array = np.array([data.eNrmzMeanConfEvent.loc[i]])
        normalized_arr = preprocessing.normalize(x_array)
        mean = np.mean(normalized_arr[0]).item()
        data.at[i,'N_eNrmzMeanConfEvent'] = mean
        
        x_array = np.array([data.eNrmzMeanConfDetail.loc[i]])
        normalized_arr = preprocessing.normalize(x_array)
        mean = np.mean(normalized_arr[0]).item()
        data.at[i,'N_eNrmzMeanConfDetail'] = mean
    
        
    data.at[i,'participant'] = n                   # inserting the participant num col
    n += 1
    mean_cols = ['participant','NrmzMeanConfPair','NrmzMeanConfEvent','NrmzMeanConfDetail','N_eNrmzMeanConfPair','N_eNrmzMeanConfEvent',
                 'N_eNrmzMeanConfDetail','iEvent','iBlock']
    df = pd.DataFrame(data.groupby('iEvent')[mean_cols].mean(), columns=mean_cols)
    
    df['ppNum'] = data['participant']
    df = df.astype({'iEvent':"int",'iBlock':"int"})
    li.append(df)                           # appending all the data gathered in a list
    
# converting the list into a dataframe

df = pd.concat(li, axis=0, ignore_index=True)

    
df = df[['ppNum','NrmzMeanConfPair','NrmzMeanConfEvent','NrmzMeanConfDetail','N_eNrmzMeanConfPair','N_eNrmzMeanConfEvent',
         'N_eNrmzMeanConfDetail','iEvent','iBlock']]
'''
# dropping unwanted cols
df.drop(['latency','rank','sac_angle','eNrmzMeanConfPair','eNrmzMeanConfEvent','eNrmzMeanConfDetail','eSumCorConfPair'
            ,'eSumCorConfEvent','eSumCorConfDetail','eNrmzMeanConfPair_EventOnset2bins','eNrmzMeanConfEvent_EventOnset2bins'
            ,'eNrmzMeanConfDetail_EventOnset2bins','eCorScorePair_EventOnset2bins','eCorScoreEvent_EventOnset2bins',
            'eCorScoreDetail_EventOnset2bins','eSumCorConfPair_EventOnset2bins','eSumCorConfEvent_EventOnset2bins',
            'eSumCorConfDetail_EventOnset2bins'], inplace=True, axis=1)

# dropping NaNs
df = df.dropna()
'''
#convert df to csv
df.to_csv( "merged_avg.csv", index=False, encoding='utf-8-sig')


#==================================================================================
