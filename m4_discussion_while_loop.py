import csv

csv_reader = csv.reader("sample_data/employees_data.csv")

for r in csv_reader:
    print(r)
