#! /usr/bin/env python3
import csv
import os
import sys
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

dataPath = '../data' 
fileNames = ['23-02-2018.csv']

df = pd.read_csv(os.path.join(dataPath, fileNames[0]))

for name in fileNames[1:]:
    fname = os.path.join(dataPath, name)
    print('appending:', fname)
    df1 = pd.read_csv(fname)
    df = df.append(df1, ignore_index=True)

df = shuffle(df)
print('creating binary file')
df['Label'] = df['Label'].map(
    {'Benign': 'Benign', 'Brute Force -Web': 'Malicious', 'Brute Force -XSS': 'Malicious',
     'SQL Injection': 'Malicious'})

outFile = os.path.join(dataPath, 'ids_binary_data')
df.to_csv(outFile + '.csv', index=False)