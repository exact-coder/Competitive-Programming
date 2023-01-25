""" input
2 4
output
4
input
3 3
output
4 """

m,n = input().split()

rectLen = int(m) * int(n)
numberOfDominoes = (rectLen / 2)
convert = int(numberOfDominoes)

print(convert)
