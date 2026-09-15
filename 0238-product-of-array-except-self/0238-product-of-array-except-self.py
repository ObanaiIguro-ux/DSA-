class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #array to store all left multiplication
        left = [1]*n
        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]
        
        #array tp store all right multiplication
        right = [1]*n
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]

        result = [1]*n
        for i in range(n):
            result[i] = left[i]*right[i]

        return result
        