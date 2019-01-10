import csv
 
with open('./05_Files/Examples/datos_2.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for (first_name, last_name) in reader:
        print(first_name, last_name)
# Jose 912349817234
# Juan 912349817234
# Manuel 912349817234     