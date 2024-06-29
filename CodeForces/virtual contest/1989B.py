

num_case = int(input())

for i in range(num_case):
    a_substring = list(input())
    b_subsequence = list(input())
    len_a = len(a_substring)
    len_b = len(b_subsequence)

    for j in range(len_b):
        
        start = j
        common = 0
        for k in range(k<len_a):
            if a_substring[k] == b_subsequence[start]:
                start+=1
                common+=1
            print((len_a+len_b)-common)


    

    