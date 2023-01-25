# def listMaker(inp):
#     return list(inp)

# list1 = listMaker(input().lower())
# list2= listMaker(input().lower())

# # print(a,b)
# # print(list1)
# for i in range(len(list1)):
#     if ord(list1[i])> ord(list2[i]):
#         print(1)
#         break
#     elif ord(list1[i]) < ord(list2[i]):
#         print(-1)
#         break
#     elif list1 == list2:
#         print(0)
#         break

val1 = input().lower()
val2 = input().lower()

if(val1 < val2):
    print("-1")
elif(val1 > val2):
    print("1")
elif(val1 == val2):
    print("0")
