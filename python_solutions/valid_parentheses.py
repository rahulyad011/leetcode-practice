class Solution:
    def isValid(self, s: str) -> bool:
        """
        Hint: use stack, check last enter bracket
        if checking close to open bracket then reverse the string
        else make the mapping dict opposite(key, value)
        """

        stack = []
        bracket_map = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                if bracket_map[char] != stack[-1]:
                    return False
                else:
                    stack.pop(-1)
        if stack:
            return False
        else:
            return True