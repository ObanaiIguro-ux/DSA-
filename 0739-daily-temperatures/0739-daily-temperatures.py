class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0]*n     #default i give 0 value to my array
        stack = []

        for i in range(n-1,-1,-1): #moving in reverse order
            #popping all indices with a lower
            #or equal temp then the current index
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            #if the stack still has elements,
            #then the next warmer temperature exists
            if stack:
                result[i] = stack[-1] - i
            
            #inserting current index in the stack
            stack.append(i)
        return result
