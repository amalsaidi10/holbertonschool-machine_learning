df = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
df = df[df['Close'].notna()]
df.head()
