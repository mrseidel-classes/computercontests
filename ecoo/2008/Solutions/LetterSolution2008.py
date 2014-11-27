def dist(a, b):
    if a[0] - b[0] == 0 and a[1] - b[1] == 0:
        return 0
    return 1.0/pow(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2),0.5)

file = open("DATA31.txt", 'r')
f = file.readlines()

arr = []
letters = []
for line in f:
    if len(line) > 2:
        arr.append(line[:-1])
    if len(line) <=2:
        if '\n' in line:
            letters.append(line[:-1])
        else:
            letters.append(line)

for letter in letters:
    calc = 0
    positions = []
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] == letter:
                positions.append((y+1, x+1))

    for i in range(len(positions)):
        for j in range(len(positions)):
            calc += dist(positions[i], positions[j])
    
    print("the " + letter + "-solution = %.4f" % calc)    
