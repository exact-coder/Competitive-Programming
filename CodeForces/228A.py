

horseshoes = list(map(int, input().split()))

coloringShoes = []

for i in range(len(horseshoes)):
    s = horseshoes[i]
    if s not in coloringShoes:
        coloringShoes.append(s)
print(len(horseshoes) - len(coloringShoes))