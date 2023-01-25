
totalPolyhedron = int(input())
""" "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20 """
output = 0
polyhedron = []

for i in range(totalPolyhedron):
    singleHedron = input()
    polyhedron.append(singleHedron)

for j in range(len(polyhedron)):
    singleElement = polyhedron[j]
    if(singleElement == "Tetrahedron"):
        output += 4
    elif(singleElement == "Cube"):
        output += 6
    elif(singleElement == "Octahedron"):
        output += 8
    elif(singleElement == "Dodecahedron"):
        output += 12
    elif(singleElement == "Icosahedron"):
        output += 20
    else:
        pass
print(output)
