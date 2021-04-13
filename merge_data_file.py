import pandas as pd
import glob
import os
from sklearn.utils import shuffle

path = "../data"
fileName = 'data.csv'
allFiles = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f) for f in allFiles)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
concatenated_df = shuffle(concatenated_df)
concatenated_df.to_csv(path + '/data.csv', index=False)