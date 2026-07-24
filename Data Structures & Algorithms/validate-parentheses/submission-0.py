from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        connect_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        open_set = set(connect_map.values())
        close_set = set(connect_map.keys())

        for c in s:
            if c in open_set:
                stack.append(c)
                
            elif c in close_set:
                if not stack:
                    return False
                new_open_char = stack.pop()
                new_open_char_check = connect_map.get(c, None)
                if not new_open_char or (new_open_char != new_open_char_check):
                    return False
            
        if len(stack) >= 1:
            return False

        return True

            