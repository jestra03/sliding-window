# Programming Techniques: Sliding Window
# Name: Joshua Estrada

# given a string, return first index of substring
def find_substring(string:str, s:str)->int:
    if len(s) > len(string):  # substring larger than main string, return -1
        return -1
    for i in range(0, len(string) + 1 - len(s)):
        start_i = i
        k = 0
        for j in range(len(s)):
            if string[j] != s[k]:
                start_i = -1
                break
            k += 1
        if start_i != -1:
            break
    return start_i