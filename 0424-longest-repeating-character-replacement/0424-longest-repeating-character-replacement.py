class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        start,max_length,max_repeat = 0,0,0

        for end in range(len(s)):
            #increment character count and handle case when key doesn't exist
            count[s[end]] = count.get(s[end],0) + 1

            #max_repeat is the character with highest frequency
            max_repeat = max(max_repeat, count[s[end]])

            #if character that need to be replaced exceeds k, shrink the window
            window = end - start + 1
            if(window - max_repeat) > k:
                count[s[start]] -= 1
                start += 1

            window = end - start + 1
            max_length = max(max_length,window)
        return max_length