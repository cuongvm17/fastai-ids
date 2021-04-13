import csv
import sys
import datetime
from dateutil import parser
import os

path = '../data/'
fileName = 'data.csv'
outputFile = 'dataCleaned.csv'
        
def cleanData(fileClean):
    count = 1
    dataFile = []
    with open(fileClean, 'r') as csvfile:
        data = csvfile.readlines()
        header = data[0].split(',')
        header = header[4:]
        header = ','.join(header)
        totalRows = len(data)

        for line in data[1:]:
            line = line.strip()
            cols = line.split(',')
            cols = cols[4:]
            dt = parser.parse(cols[2])
            time = (dt - datetime.datetime(1970, 1, 1)).total_seconds()
            cols[2] = str(time)
            line = ','.join(cols)
            dataFile.append(line)

    with open(path + outputFile, 'w') as csvoutfile:
        csvoutfile.write(header)
        for line in dataFile:
            csvoutfile.write('{}\n'.format(line))


cleanData(path + fileName)
