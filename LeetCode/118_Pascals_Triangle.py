
def generate(numRows):
    if numRows == 0:
        return []

    output = []
    output.append([1])

    for row in range(1, numRows):
        r = []
        prevList = output[row - 1]
        r.append(1)

        for j in range(1, row):
            r.append(prevList[j - 1] + prevList[j])
        
        r.append(1)
        output.append(r)

    return output

print(generate(5))
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(generate(1))
print(generate(2))
# [[1]]


