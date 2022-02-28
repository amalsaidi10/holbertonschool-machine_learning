import pandas as pd
def from_file(filename, delimiter):
  df=pd.read_csv(filename,delimiter=delimiter)
  return df
df1 = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
print(df1.head())
df2 = from_file('/content/drive/MyDrive/bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv.zip', ',')
print(df2.tail())
