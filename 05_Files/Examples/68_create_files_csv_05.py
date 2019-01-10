import csv
with open('./05_Files/Examples/datos_3.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
          print(row['first_name'], row['last_name'])