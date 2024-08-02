
# https://leetcode.com/problems/climbing-stairs/description/


def climbStairs(n):
    
    if (n == 0): return 1
    if (n == 1): return 1

    prev = 1
    prev2 = 1

    for i in range(1,n):
        current = prev + prev2
        prev2 = prev
        prev = current
    return prev

print(climbStairs(4))