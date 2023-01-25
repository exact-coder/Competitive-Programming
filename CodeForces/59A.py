

givenWord = input()
capitalNumLen = 0
lowerNumLen = 0

for i in range(len(givenWord)):
    singleletter =ord(givenWord[i])
    if(singleletter > 64 and singleletter < 91):
        capitalNumLen += 1
    elif(singleletter >96 and singleletter < 123):
        lowerNumLen += 1
if(capitalNumLen < lowerNumLen or capitalNumLen == lowerNumLen):
    print(givenWord.lower())
elif(capitalNumLen > lowerNumLen):
    print(givenWord.upper())
