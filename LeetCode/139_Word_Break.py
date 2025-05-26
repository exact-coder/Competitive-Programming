

def wordBreak(s, wordDict):
    dp = [False] * (len(s)+1)
    dp[0] = True
    wordSet = set(wordDict)

    for i in range(1, len(s) + 1):
        for j in range(i-1,-1,-1):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[len(s)]


print(wordBreak("leetcode",["leet","code"]))
# Output: true
print(wordBreak("applepenapple",["apple","pen"]))
# Output: true
print(wordBreak("catsandog",["cats","dog","sand","and","cat"]))
# Output: false

