class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []
        def dfs(index, current_combination, current_sum):
            #If the curr sum equals the target, we have found valid combination
            if current_sum == target:
                all_combinations.append(current_combination)
                return
            #if we have considered all candidates or current sum exceeds target, backtrack
            if index >= len(candidates) or current_sum > target:
                return 
            #include current candidate, reuse allowed
            dfs(index, current_combination + [candidates[index]], current_sum + candidates[index])
            #skip current candidate
            dfs(index + 1, current_combination, current_sum)
        dfs(0, [], 0)
        return all_combinations