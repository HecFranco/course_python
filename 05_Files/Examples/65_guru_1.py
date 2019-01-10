# f = open("textfile.txt","w+") # Separa e incluye líneas intermedias
f = open("textfile.txt","w+", newline='')
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()