file = open("DATA11.txt", 'r')
f = file.readlines()
for line in f:
    start, end = line.split(" ")
    pages = 0
    digits = 0
    for i in range (int(start), int(end)+1):
        pages += 1  
        digits += len(str(i))   
    print("There are " + str(digits) + " digits used to number the " 
          + str(pages) + " pages")