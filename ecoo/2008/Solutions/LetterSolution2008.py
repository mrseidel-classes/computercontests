def calculation(a, b, x2, y2):
    return 1/sqrt(pow((a - x), 2) + pow((b - y), 2))

file = open("DATA31.txt", 'r')
f = file.readlines()

arr = []
letters = []
for line in f:
    print(line)
    if len(line) > 2:
        arr.append(line[:-1])
    if len(line) <=2:
        if '\n' in line:
            letters.append(line[:-1])
        else:
            letters.append(line)
               
print(arr)
print(letters)