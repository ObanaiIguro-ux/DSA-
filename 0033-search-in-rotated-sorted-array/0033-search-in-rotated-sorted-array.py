class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            #checks if mid == target
            if nums[mid] == target:
                return mid      #returns if target found
            
            #if the left half is sorted
            if nums[mid] >= nums[left]:
                #check is target lies in the left half(range)
                if nums[left] <= target < nums[mid]:
                    right = mid - 1     #narrow down to left half
                else: 
                    left = mid + 1      #narrow down to right half
            
            #if right half is sorted
            else:
                #check if target lies in the right half(range)
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  #narrow down to right half
                else:
                    right = mid - 1   #narrow down to left half
        #target not found
        return -1  
