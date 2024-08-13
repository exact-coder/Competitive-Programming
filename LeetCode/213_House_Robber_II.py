
def rob(nums):
    rob1 =0
    rob2=0
    max1=nums[0]
    max2=0
    length = len(nums)

    for i in range(length-1):
        max1 = max(rob1+nums[i],rob2)
        rob1 = rob2
        rob2 = max1
    
    rob1 =0
    rob2 =0

    for i in range(1,length):
        max2 = max(rob1+nums[i],rob2)
        rob1 = rob2
        rob2 = max2
    
    return max(max1,max2)

print(rob([2,3,2]))
# 3
print(rob([1,2,3,1]))
# 4