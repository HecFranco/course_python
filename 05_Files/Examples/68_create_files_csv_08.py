import csv
 
results = []
with open('./05_Files/Examples/datos_3.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    print (results) 
# [
#   OrderedDict(
#       [
#           ('first_name', 'Alex'),
#           ('last_name', 'Brian'),
#           ('Grade', 'B')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Rachael'), 
#           ('last_name', 'Rodriguez'), 
#           ('Grade', 'A')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Jane'), 
#           ('last_name', 'Oscar'), 
#           ('Grade', 'B')
#       ]
#   ), 
#   OrderedDict(
#       [
#           ('first_name', 'Jane'),
#           ('last_name', 'Loive'), 
#           ('Grade', 'B')
#       ]
#   )
# ]