import csv
 
with open('./05_Files/Examples/datos_6.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},
                      {'Grade': 'A', 'first_name': 'Rachael',
                          'last_name': 'Rodriguez'},
                      {'Grade': 'C', 'first_name': 'Tom', 'last_name': 'smith'},
                      {'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},
                      {'Grade': 'A', 'first_name': 'Kennzy', 'last_name': 'Tim'}])
 
print("writing complete")