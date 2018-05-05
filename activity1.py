import os
import csv

cereal(1)_csv_path=os.path.join(".","Resource", "cereal(1).csv")

with open(cereal(1)_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    for row in csv_reader:
        if float(row[7]) >=5):
            print(row)
            
    