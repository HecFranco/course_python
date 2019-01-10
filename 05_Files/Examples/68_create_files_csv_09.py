import csv
 
myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]
 
myFile = open('./05_Files/Examples/datos_4.csv', 'w', newline='')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")