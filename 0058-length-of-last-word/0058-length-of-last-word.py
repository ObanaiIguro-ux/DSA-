class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        #uses O(n) TC and SC
        words = s.split()
        return len(words[-1])
        '''
        #Uses O(n) TC but O(1) SC
        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        
        count = 0
        while i >= 0 and s[i]!=' ':
            count += 1
            i -= 1
        
        return count