class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                #according to ques i want to print 1 index but python stores it as 0 indexed
                return [left+1,right+1]
            elif current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
        return []