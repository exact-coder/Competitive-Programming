

total_test = int(input())
for i in range(total_test):
    n_GB,k_sec = map(int,input().split())
    print(1 + ((n_GB-1) * k_sec))
