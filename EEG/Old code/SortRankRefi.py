###DO NOT CHANGE ANYTHING HERE###
import pandas as pd

#==================================================================================


path = "D:\\dibs\\your_todays_version\\"


# joining files as a list
#csv_files = glob.glob(os.path.join(path, "merged_refi.csv"))

df = pd.read_csv(path+"merged_refi.csv",sep=';')
df = df.dropna()
indexNames = df[df['Refi'] == 'bpF' ].index  
df.drop(indexNames , inplace=True)

gdf = df.groupby('Refi')

lst = [gdf.get_group(x) for x in gdf.groups]

for i in range (0,(len(lst)-1)):
    dfitem = lst[i]
    dfitem.to_csv(path+'Res\\'+str(i)+'.csv', sep=';')