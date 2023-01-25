

inputYear = input()
nextYear = int(inputYear) + 1
makeStr = str(nextYear)
distinctYear = set(makeStr)
def distinctFinder (nextYear,distinctYear):
    if(len(distinctYear) > 3):
        print(nextYear)
    else:
        makeInt = int(nextYear)
        makeInt += 1
        inputYear = makeInt
        k = str(inputYear)
        distinctYear = set(k)
        distinctFinder(inputYear,distinctYear)

distinctFinder(nextYear,distinctYear)

# inputYear = input()


# for i in range(1000):
#     ele = int(inputYear) + i
#     makeList =list(ele)
#     if (makeList[i] == makeList[i + 1]):
#         continue
#     else:
#         print(ele)




