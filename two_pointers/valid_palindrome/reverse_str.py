class Solution: 
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]
    
    
s = "A man, a plan, a canal: Panama"
csl = Solution()
print(csl.isPalindrome(s))