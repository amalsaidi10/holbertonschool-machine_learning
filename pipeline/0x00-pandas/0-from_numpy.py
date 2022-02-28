#!/usr/bin/env python3
import numpy as np
import pandas as pd
import string
def from_numpy(array):
  num_columns=array.shape[1]
  alphabet_string = string.ascii_uppercase
  list_alphabet=list(alphabet_string)
  col= list_alphabet[:num_columns]
  df=pd.DataFrame(array,columns=col)
  return df
