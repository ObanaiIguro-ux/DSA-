class Solution:
    def isValid(self, s: str) -> bool:
        #initialize an empty stack to keep track of opening backets
        stack = []

        #mapping of closing brackets to their corresponding opening brackets
        bracket_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        #iterate through each characters in the string
        for character in s:
            if character in bracket_map:
                if stack and stack[-1] == bracket_map[character]:
                    stack.pop()
                else:
                    return False
            else:
        #if the character is an opening bracket, pushed it onto the stack
                stack.append(character)
        #after processing all characters, 
        #return True if the stack is empty(all brackets matched), else False
        return not stack