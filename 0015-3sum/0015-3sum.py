class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #check if array is null or has less than 3 elements
        if nums is None or len(nums) < 3:
            return []
        
        #sort the elements
        nums.sort()
        
        #Use a set to keep unique triplets
        result = set()

        #Fix the i'th element and find the other two element
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1

            while left < right:
                target = nums[i] + nums[left] + nums[right]

                if target == 0:
                    #Add the triplet on the set
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
        return list(map(list,result))