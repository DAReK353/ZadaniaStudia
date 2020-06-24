import time

while True:
    filename = input("Enter the file name... ")
    try:
        if ".csv" in filename:
            file = open(filename)
            break
        else:
            filename = filename + ".csv"
            file = open(filename)
            break
    except FileNotFoundError:
        print("File not found.")

startime = time.time()
rawheader = file.readline()
rawheader = rawheader.strip()
if "," in rawheader:
    rawheader = rawheader.split(",")
    option = 1
else:
    rawheader = rawheader.split(";")
    option = 2

countheader = len(rawheader)
datafromfile = []
countlines = 0
for line in file:
    line = line.strip()
    if option == 1:
        line = line.split(",")
    else:
        line = line.split(";")
    datafromfile.append(line)
    countlines += 1

file.close()

elapsedtime = time.time() - startime

print("End of reading data.")
print("Number of columns:", countheader)
print("There is", countlines, "data for each column.")
print("There are", countlines * countheader, "results in total.")
print("Total time:", elapsedtime, "seconds")
while True:
    print("=================================")
    print("What do you want to do now?")
    print("1. See data from the selected column")
    print("2. Save file.")
    print("3. Exit.")
    useroption = input("Enter the correct number: ")
    if useroption == "1":
        print("Which column do you want to see?")
        print("Available columns:")
        count = 1
        for i in rawheader:
            print(count, ". ", i)
            count += 1
        useroption = input("Enter the correct number: ")
        useroption = int(useroption)
        useroption -= 1
        fromlist = 0
        datafromonecolumn = []

        while fromlist < countlines:
            data = datafromfile[fromlist][useroption]
            datafromonecolumn.append(data)
            fromlist += 1

        print(datafromonecolumn)

    if useroption == "2":
        print("Enter the file name under which you want to save the file: ")
        savefile = input()
        countforcolumn = 0
        for i in rawheader:
            i = i.strip()
            file = open(savefile + i + ".txt", "w+")
            file.write(i)
            file.write("\n")
            for x in datafromfile:
                x = x[countforcolumn]
                x = x.strip()
                file.write(x)
                file.write("\n")
            countforcolumn += 1
            file.close()
    if useroption == "3":
        exit()
