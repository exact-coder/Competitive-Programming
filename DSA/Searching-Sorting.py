

def liner_serach(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return "Item Not Found"

arr = [15,12,28,19,36]
result =liner_serach(arr,28)
# print(result)

# Binary search with recursion
def binary_search(arr,low,high,item):
    
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
    else:
        return -1
arr = [11,58,65,22,33,44,55,66,77,88,99,100]

# print(binary_search(arr,0,len(arr)-1,10))

# Sorting
def is_sorted(arr):
    sorted = True

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

# print(is_sorted(arr))

# Monkey Sort and Sleep Sort is a joke 
import random,time
def monkey_sort(arr):
    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)
# monkey_sort(arr)

# Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)-1):
        flag =0
        for j in range(len(arr)-1 -i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag=1
        if flag ==0:
            break
    print(arr)
arr = [10,5,1,4,7,2,50]
# bubble_sort(arr)

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr) -1):
        min = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    print("Selection Sort :",arr)

# selection_sort(arr)

# Merged Sort
def merge_sorted(arr1,arr2):
    i = j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while i < len(arr1):
        merged.append(arr1[i])
        i+=1
    while j > len(arr2):
        merged.append(arr2[j])
        j+=1
    return merged


# arr1 = [10,5,1,4,7,2,50]
# arr2 = [12,8,6,3,9]

# merge_sorted(arr1,arr2)
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sorted(left,right)

arr =[10,5,1,4,7,2,50,12,8,6,3,9,15,17]
print(merge_sort(arr))


# Watching vedio length 10.57min