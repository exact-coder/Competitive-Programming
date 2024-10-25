# Abstraction means hiding the implementation details of a class and only showing the essential features to the users.
# class Car:

#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car Started....")

# car1=Car()
# car1.start()
# here, Before the started the car run two process:clutch and acclerate then the car start but only the user see that the car is started.Abstraction hides those two process.



#Q: Sum of numbers 1 to N

# 1. Recursive way :
def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n-1)+n
print(sum(50))

# 2. Using loop
def sum(n):
    res =0
    i=0

    while i<= n:
        res +=i
        i+=1
    return res
print(sum(50))

# or
def sum(n):
    res =0
    for i in range(n+1):
        res +=i
    return res
print(sum(50))
# 3. Arithmetic (Best Approach)
def sum(n):
    return n * (n+1) // 2
print(sum(50))


# Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if arr[mid] < x:
			low = mid + 1

		# If x is smaller, ignore right half
		elif arr[mid] > x:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1



arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
