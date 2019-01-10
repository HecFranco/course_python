import csv
doc_csv = open('./05_Files/Examples/datos_1.csv', 'w', newline='')  
csv_data = csv.writer(doc_csv)
list = [ "Jose", 912349817234 ]
csv_data.writerow(list)
