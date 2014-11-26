def isAnagram(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    try:
        for i in s1:
            for j in s2:
                if i == j:
                    s1[s1.index(i)] = ''
                    s2[s2.index(j)] = ''
    except: #can't find the item in the second list
        return False
    return True

def findOccurences(s, ch):
    if ch == ' ': #if it's a space, skip the math
        return [-1]
    return [i+1 for i, letter in enumerate(s) if letter == ch]

file = open("DATA21.txt", 'r')
f = file.readlines()
file.close()

allowedCharacters = "abcdefghijklmnopqrstuvwxyz "

for line in f:
    first, second = line.split(" = ")
    if '\n' in second:
        second = second[:-1]
    
    origFirst = first
    origSecond = second
    
    first = first.lower()
    second = second.lower()
    
    for i in first:
        if i not in allowedCharacters:
            first.replace(i, ' ')    

    for i in second:
        if i not in allowedCharacters:
            second.replace(i, ' ')

    print (origFirst + " = " + origSecond)
    if isAnagram(first, second):
        print (" " * 8 + "is an anagram and its value is ", end='')
    
        totalValue = 0
        
        for i in range(len(first)):
            places = findOccurences(second, first[i])
            if (places[0] == 0):
                totalValue = 0
                break
            value = 0
            for num in places:
                if num != -1:
                    value += num * (i + 1)
            totalValue += value
        print(totalValue)
    else:
        print (" " * 8 + "is not an anagram")
        