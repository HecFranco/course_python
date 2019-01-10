import csv
doc_csv = open('./05_Files/Examples/datos_2.csv', 'w', newline='')  
csv_data = csv.writer(doc_csv)
list = [[ "Jose", 912349817234 ],[ "Juan", 912349817234 ],[ "Manuel", 912349817234 ]]
for element in list:
    csv_data.writerow(element)