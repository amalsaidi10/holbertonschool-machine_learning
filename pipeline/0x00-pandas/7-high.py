df = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
d1=df.sort_values('High',ascending=False)
d1.head(15)
