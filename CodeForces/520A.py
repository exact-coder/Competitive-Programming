

wordLen = int(input())
alphabet = []
word = input()
w = word.lower()

for i in range(wordLen):
    if(w[i] not in alphabet):
        alphabet.append(w[i])
    else:
        pass
if(len(alphabet) >= 26):
    print("YES")
else:
    print("NO")