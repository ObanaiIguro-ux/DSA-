class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialize the pointers and the set 
        start,end,max_length = 0,0,0
        char_set = set()

        while end < len(s):
            if s[end] not in char_set:
                char_set.add(s[end])
                max_length = max(max_length, end - start + 1)
                end += 1
            else:
                char_set.remove(s[start])
                start += 1
        return max_length