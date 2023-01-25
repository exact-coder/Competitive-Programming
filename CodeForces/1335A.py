
totalTestCase = int(input())

for i in range(totalTestCase):
    candies = int(input())
    if candies > 2 and candies % 2 != 0 :
        print(candies // 2)
    elif candies > 2:
        print((candies // 2) -1)
    else:
        print(0)

        


