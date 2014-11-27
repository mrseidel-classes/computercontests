arr = [6, 12, 44, 7, 20]


x = 3
i = 3
#find the value of the 3rd value for vals
while (float(i*pow(x,5)/pow((x-1),5)+1) != int(i*pow(x,5)/pow((x-1),5)+1)):
    i += 1

#place in value for x = i = 3
vals.append(int(i*pow(x,5)/pow((x-1),5)+1)-x) 

#values 0, 1, and 2 are placeholders - values under the 5 men won't matter anyways
vals = [0, 1, 2, 241]

#create the rest of the values based on a pattern
for i in range(4,50):
    vals.append(int((vals[i-1]+(i-2))*pow(i,5)/pow((i-1),5)-(i-1)))

#print out the requested values from the original "file" (used "arr" list to hold them for this solution)
for i in range(len(arr)):
    print("For " + str(arr[i]) + " men, the smallest number of coconuts is " + str(vals[arr[i]]))



'''
Used to find pattern for above...

for x in arr:
    i = x
    while (float(i*pow(x,5)/pow((x-1),5)+1) != int(i*pow(x,5)/pow((x-1),5)+1)):
        i += 1
    n = i*pow(x,5)/pow((x-1),5)+1
    print(str(i) + " : " + str(int(n-x)) + " -- For " + str(x) + " men, the smallest number of coconuts is " + str(int(n-x)))
         #   break
'''