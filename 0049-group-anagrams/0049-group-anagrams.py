class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        hashmap = {}

        def get_freq_string(element):
            freq_list = [0]*26

            for char in element:
                freq_list[ord(char) - ord('a')] += 1

            freq_string = []
            char = 'a'
            for position in freq_list:
                freq_string.append(char)
                freq_string.append(str(position))
                char = chr(ord(char) + 1)
            return ''.join(freq_string)

        for element in strs:
            freq_string = get_freq_string(element)

            if freq_string not in hashmap:
                hashmap[freq_string] = []
            hashmap[freq_string].append(element)
            
        return list(hashmap.values())