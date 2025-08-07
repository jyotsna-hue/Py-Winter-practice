def isPalindrome(self, s: str) -> bool:
    def alphaNum(c):
        return 'a'<=c.lower()<='z' or '0'<=c<='9'
    l,r=0,len(s)-1
    while(l<r):
        while l<r and not alphaNum(s[l]):
            l=l+1
        while l<r and not alphaNum(s[r]):
            r=r-1
        if(s[l]!=s[r]):
            return False
    l=l+1
    r=r-1
    return True 

