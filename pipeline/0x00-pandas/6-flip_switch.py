df = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
d=df.T     # transpose the dataframe
display(d[d.columns[::-1]].tail(8))  # reverse data and display just the last 8 rows 
