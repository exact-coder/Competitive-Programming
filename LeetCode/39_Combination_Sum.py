

def combinationSum(candidates, target):
    res = []
    combination =[]
    backTrack(target,res,combination,0,candidates)
    return res

def backTrack(target,res,combination,start,candidates):

    if target == 0:
        res.append(list(combination))

    elif target <0:
        return
    for i in range(start, len(candidates)):
        combination.append(candidates[i])
        backTrack(target - candidates[i], res, combination, i, candidates)
        combination.pop()


print(combinationSum([2,3,6,7],7))
# [[2,2,3],[7]]
print(combinationSum([2,3,5],8))
# [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum([2],1))
# []