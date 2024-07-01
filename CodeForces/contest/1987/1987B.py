
# num_test = int(input())
# arr = []

# for i in range(num_test):
    
n_arr_len = int(input())
arr = list(map(int,input().split()))

temp = []
final_nondec_coin =1

for i in range(n_arr_len):
    if arr[i] > arr[i+1]:
        arr[i] = arr[i+1]
        arr[i+1] = arr[i]
        final_nondec_coin +=1
        