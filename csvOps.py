import csv
from DBoperations import *


def saveUsersCSV(fileName='./csv files/user_det.csv'):
    print("Fetching user information from database...", end='\r')
    result = getAllUsersCSV()
    print("Information fetched.                      ")
    print("Saving data in csv file...", end='\r')
    outfile = open(fileName, 'w')
    outcsv = csv.writer(outfile, escapechar=' ', quoting=csv.QUOTE_NONE)
    outcsv.writerow(result[0])
    outcsv.writerows(row for row in result[1])
    print("\rData saved in csv file.   ")
    outfile.close()

saveUsersCSV()