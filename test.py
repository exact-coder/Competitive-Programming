import re

def rstrstr(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s2_len > s1_len:
        return None
    for i in range(s1_len - s2_len, -1, -1):
        if s1[i:i+s2_len] == s2:
            return s1[i:]
    return None

v = input()
a1 = input()
a2 = input()

if a1 in v and a2 in v and len(v) >= (len(a1) + len(a2)):
    a1_index = v.index(a1)
    a2_index = v.index(a2)
    if a1_index <= a2_index and rstrstr(v, a1) >= rstrstr(v, a2): # type: ignore
        print("both")
    elif a1_index > a2_index:
        print("backward")
    elif a1_index < a2_index:
        print("forward")
    else:
        print("fantasy")
else:
    print("fantasy")