class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        s = s.lower()
        for i in s:
            if i.isalnum():
                word += i
        return word[::-1] == word