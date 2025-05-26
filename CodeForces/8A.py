from typing import List

def match(text: str, pat1: str, pat2: str) -> bool:
    m, n, o = len(pat1), len(text), len(pat2)
    for i in range(n):
        for j in range(m):
            if i + j >= n or text[i + j] != pat1[j]:
                break
            if j == m - 1:
                i += m
                while i < n:
                    for j in range(o):
                        if i + j >= n or text[i + j] != pat2[j]:
                            break
                        if j == o - 1:
                            return True
                    i += 1
    return False

def revmatch(text: str, pat1: str, pat2: str) -> bool:
    m, n, o = len(pat1), len(text), len(pat2)
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if i - j < 0 or text[i - j] != pat1[j]:
                break
            if j == m - 1:
                i -= m
                while i >= 0:
                    for j in range(o):
                        if i - j < 0 or text[i - j] != pat2[j]:
                            break
                        if j == o - 1:
                            return True
                    i -= 1
    return False

def main():
    text = input()
    pattern1 = input()
    pattern2 = input()
    forward = match(text, pattern1, pattern2)
    reverse = revmatch(text, pattern1, pattern2)
    if forward and not reverse:
        print("forward")
    elif forward and reverse:
        print("both")
    elif not forward and reverse:
        print("backward")
    else:
        print("fantasy")

if __name__ == "__main__":
    main()
