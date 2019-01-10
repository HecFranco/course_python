import csv
with open('./05_Files/Examples/datos_1.csv','r', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)
File.close()