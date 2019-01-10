import csv
 
with open('./05_Files/Examples/datos_3.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)
# ['first_name', 'last_name', 'Grade']
# ['Alex', 'Brian', 'B']
# ['Rachael', 'Rodriguez', 'A']
# ['Jane', 'Oscar', 'B']
# ['Jane', 'Loive', 'B']        