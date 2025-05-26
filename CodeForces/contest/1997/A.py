

test_case = int(input())

def c_time(s):
    t = 2 
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            t += 1  
        else:
            t += 2
    return t


while test_case:
    s = input()
    output_pass = ""
    max_time = -1

    for i in range(len(s) + 1):
        for c in range(ord('a'), ord('z') + 1):
            new_pass = s[:i] + chr(c) + s[i:]
            new_time = c_time(new_pass)
            if new_time > max_time:
                max_time = new_time
                output_pass = new_pass

    print(output_pass)
    test_case-=1






