
nums = list(map(int,input("Give a List of Number:").split(",")))
target = int(input("Give the target Number:"))

def twoSum(nums: list[int], target:int):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                print([i,j])

twoSum(nums,target)
