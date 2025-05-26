

def rob(nums):
    
    rob1 = 0
    rob2 = 0
    max_ele =0

    for i in range(len(nums)):
        max_ele = max(rob1+nums[i],rob2)
        rob1 = rob2
        rob2 = max_ele
    return max_ele

print(rob([1,2,3,1]))
# 4
print(rob([2,7,9,3,1]))
# 12
