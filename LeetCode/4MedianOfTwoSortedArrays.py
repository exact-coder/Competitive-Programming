import math
nums1 = list(input())
nums2 = list(input())

totalLen = len(nums1) + len(nums2)
isEven = False

finalList = []

if totalLen % 2 ==0:
    value = totalLen // 2
    isEven = True
    count = -1
else:
    value = math.ceil(totalLen/2)
    count =0
i,j =0,0

while (i < len(nums1) and j < len(nums2)):
    if nums1[i] < nums2[j]:
        finalList.append(nums1[i])
        count +=1 
        i+=1
    else:
        finalList.append(nums2[j])
        count+=1
        j+=1
    if count == value:
        if isEven == False:
            print(finalList[-1])
        else:
            print(((finalList[-1] + finalList[-2])/2))
while(i<len(nums1) and j ==len(nums2)):
    finalList.append(nums1[i])
    count += 1
    i += 1
    if count == value:
        if isEven == False:
            print(finalList[-1])
        else:
            print((finalList[-1]+finalList[-2])/2)
while(i==len(nums1) and j < len(nums2)):
    finalList.append(nums2[j])
    count += 1
    j += 1
    if count == value:
        if isEven == False:
            print(finalList[-1])
        else:
            print((finalList[-1]+finalList[-2])/2)



