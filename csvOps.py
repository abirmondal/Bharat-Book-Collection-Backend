import csv
from DBoperations import *


def saveUsersCSV(fileName='user_det.csv'):
    result = getAllUsersCSV()
    outfile = open(fileName, 'w')
    outcsv = csv.writer(outfile, escapechar=' ', quoting=csv.QUOTE_NONE)
    outcsv.writerows(row for row in result)
    outfile.close()

saveUsersCSV()