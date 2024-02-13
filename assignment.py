def palindrome(s):
    return s == s[::-1]

s = "geeks"
ans = palindrome(s)

if ans:
    print("Yes")
else:
    print("No")
