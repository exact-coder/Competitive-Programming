

initialVal = 0
operations = int(input())

for i in range(operations):
    opera = input()
    if (opera == "X++" or opera == "++X"):
        initialVal += 1
    elif (opera == "X--" or opera == "--X"):
        initialVal -= 1
print(initialVal)
