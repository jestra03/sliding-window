# Programming Techniques: Sliding Window
# Name: Joshua Estrada

# given a string, return first index of substring
def find_substring(string:str, s:str)->int:
    if len(s) > len(string):  # substring larger than main string, return -1
        return -1
    for i in range(0, len(string) + 1 - len(s)):
        start_i = i
        k = 0
        for j in range(i, i + len(s) - 1):
            if string[j] != s[k]:
                start_i = -1
                break
            k += 1
        if start_i != -1:
            break
    return start_i
    # the window is the length of the substring
    # if there is a mismatch when comparing the window to the substring, the window will stop comparing and slide one

# given an arr, a number k defining sum of n elements
def max_sum(arr:list, n:int):
    if len(arr) < n:  # arr is too small
        return -1
    total = sum(arr[0:n])
    for i in range(1, len(arr) + 1 - n):  # iterating through arr is O(n)
        temp_total = total - arr[i-1] + arr[i + n - 1]  # window is length of n, slide window in constant time O(1)
        total = max(total, temp_total)
    return total
    # faster than nested loop (brute force approach) since the sum in the window is calculated in O(1) time
    # the sum calculated is O(1) because the prev start is removed and new end is added

def max_sum_bruteforce(arr:list, n:int):
    if len(arr) < n:
        return -1
    sum = 0
    for i in range(len(arr) + 1 - n):  # O(n) operation
        temp_sum = 0
        for j in range(i, i + n):  # O(n) operation
            temp_sum += arr[j]
        sum = max(sum, temp_sum)
    return sum
    # nested loop: O(n) operation where the sum is calculated O(n) times
