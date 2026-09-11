class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return[hashmap[complement], i]
            
            #Store the current number and its index of nums in hashmap
            hashmap[nums[i]] = i