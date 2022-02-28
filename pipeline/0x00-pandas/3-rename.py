import pandas as pd
#Rename the column Timestamp to Datetime
df1.rename(columns={'Timestamp':'Datetime'},inplace=True) # inplace=true we make a change to the dataframe
df1['Datetime']=pd.to_datetime(df1['Datetime']).dt.strftime('%m/%d/%Y %H:%M:%S') # convert
df=df1[['Datetime','Close']].tail()
print(df)
