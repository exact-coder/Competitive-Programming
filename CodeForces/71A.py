"""
input
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

output
word
l10n
i18n
p43s """


def wayTooLongWords(words):
    for i in range(len(words)):
        everyWordLen = len(words[i])
        if( everyWordLen <= 10):
            print(words[i])
        else:
            for j in range(everyWordLen):
                firstLetter = words[i][j]
                lastLetter = words[i][-1]
                wordLen = everyWordLen -2
                specialAbb = firstLetter + str(wordLen) + lastLetter
                print(specialAbb)
                break


count = int(input())

word = []

for i in range(count): 
    w = input()
    word.append(w)


wayTooLongWords(word)





