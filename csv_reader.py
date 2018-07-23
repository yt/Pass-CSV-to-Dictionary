import csv

csv_file_name = 'data.csv'

with open(csv_file_name) as file:
    reader = csv.DictReader(file)
    data = [r for r in reader]


# You can't access the elements as
row_number = 0
column_name = 'Date'
print(data[row_number][column_name])
