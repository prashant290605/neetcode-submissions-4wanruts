class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counts1 = [0]*26
        counts2 = [0]*26

        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        match = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                match += 1
        
        l = 0
        for i in range(len(s1),len(s2)):
            if match == 26:
                return True
            match = 0
            counts2[ord(s2[i]) - ord('a')] += 1
            counts2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            for i in range(26):
                if counts1[i] == counts2[i]:
                    match += 1
            
        return match == 26