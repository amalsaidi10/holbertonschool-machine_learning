df = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
del df['Weighted_Price']  # remove column
df['Volume_(BTC)'].fillna(0,inplace=True)
df['Volume_(Currency)'].fillna(0,inplace=True)  # inplace=true to make changes in the current dataframe
df['Close'].fillna(method='pad',inplace=True)# "pad"fill as same as the previous row
df['High'].fillna(df['Close'],inplace=True)
df['Low'].fillna(df['Close'],inplace=True)
df['Open'].fillna(df['Close'],inplace=True)
print(df.head(15))
