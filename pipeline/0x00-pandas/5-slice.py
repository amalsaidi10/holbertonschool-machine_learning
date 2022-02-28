df = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
df3=df.iloc[::60,2:6]               # :: every 60 row 
print(df3.tail())
