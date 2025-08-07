def is_palindrome(s):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


print(is_palindrome("ana"))  
