import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('/content/drive/MyDrive/coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv.zip', ',')
df[['High','Close']].tail(10).to_numpy() #to_numpy() convert to array type
