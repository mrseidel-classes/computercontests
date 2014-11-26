file = open('DATA11.txt', 'r')
f = file.readlines()
file.close()
print(f)

for word in f:
    word = word[:-1]
    print ("* " + ''.join([str(letter) + " " for letter in word]) + "*")

    for i in range(len(word)):
        print(word[len(word)-i-1] + " *" * len(word) + " " + word[i])
    
    print ("* " + ''.join([str(letter) + " " for letter in word[::-1]]) + "*")
