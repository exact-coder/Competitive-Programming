
num_of_coin = int(input())


for c in range(num_of_coin):
    x,y = input().split()
    y = int(y)
    if y < -1:
        print("NO")
    else:
        print("YES")