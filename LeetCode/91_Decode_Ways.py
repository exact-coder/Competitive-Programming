
def numDecodings(s):
    if(s[0]== "0"): return 0
    one=1
    two=1

    for i in range(1,len(s)):
        current=0
        if(s[i] != '0'): current = one
        val = int(s[i-1:i+1])
        if val >=10 and val <= 26:
            current+=two
        
        two = one
        one = current
    return one



print(numDecodings("12"))
print(numDecodings("2"))
#2
print(numDecodings("226"))
#3
print(numDecodings("06"))
#0
