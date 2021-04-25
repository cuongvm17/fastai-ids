#! /usr/bin/env python3
import csv
import os
import sys
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

dataPath = '../data' 
fileNames = ['dataCleaned.csv']

df = pd.read_csv(os.path.join(dataPath, fileNames[0]))

for name in fileNames[1:]:
    fname = os.path.join(dataPath, name)
    print('appending:', fname)
    df1 = pd.read_csv(fname)
    df = df.append(df1, ignore_index=True)

df = shuffle(df)
print('creating binary file')
print(df.Label.unique())
# df['Label'] = df['Label'].map(
#     {'Benign': 'Benign', 'Brute Force -Web': 'Malicious', 'Brute Force -XSS': 'Malicious',
#      'SQL Injection': 'Malicious'})

df['Label'] = df['Label'].map(
    {'Benign': 'Benign', 'URL-Webshell-command': 'Webshell', 'Webshell': 'Webshell',
     'Webshell-command': 'Webshell'})
     
outFile = os.path.join(dataPath, 'webshell_binary_file2')
df.to_csv(outFile + '.csv', index=False)