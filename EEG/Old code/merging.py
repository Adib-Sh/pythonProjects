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

    df = pd.read_table(f, delimiter =";")   # read the csv file
    df['participant'] = n                   # inserting the participant num col
    n += 1
    li.append(df)                           # appending all the data gathered in a list

# converting the list into a dataframe
frame = pd.concat(li, axis=0, ignore_index=True)

# dropping NaNs
frame = frame.dropna()

frame['eNrmzMeanConfPair'] = frame['eNrmzMeanConfPair'].str.split('.')

for i, row in frame.iterrows():
    x_array = np.array([frame.eNrmzMeanConfPair.loc[i]])
    normalized_arr = preprocessing.normalize(x_array)
    mean = np.mean(normalized_arr[0]).item()
    frame.at[i,'NeNrmzMeanConfPair'] = mean
    
# dropping unwanted cols
frame.drop(['latency','rank','sac_angle','eSumCorConfPair'
            ,'eSumCorConfEvent','eSumCorConfDetail','eNrmzMeanConfPair_EventOnset2bins','eNrmzMeanConfEvent_EventOnset2bins'
            ,'eNrmzMeanConfDetail_EventOnset2bins','eCorScorePair_EventOnset2bins','eCorScoreEvent_EventOnset2bins',
            'eCorScoreDetail_EventOnset2bins','eSumCorConfPair_EventOnset2bins','eSumCorConfEvent_EventOnset2bins',
            'eSumCorConfDetail_EventOnset2bins'], inplace=True, axis=1)



#convert df to csv
frame.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


#==================================================================================
