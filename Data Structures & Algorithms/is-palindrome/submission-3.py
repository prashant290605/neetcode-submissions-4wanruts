class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        s = s.lower()
        for c in s:
            if c.isalnum() and c != ' ':
                word += c
        
        return word == word[::-1]