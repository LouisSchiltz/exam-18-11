def isPalindroom(s):
    low = 0
    high = len(s)-1

    ispalindrome = True
    while low <= high:
        if s[low] != s[high]:
            ispalindrome = False
            break
        low += 1
        high -= 1

    return ispalindrome


