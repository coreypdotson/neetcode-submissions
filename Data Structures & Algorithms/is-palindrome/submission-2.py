class Solution:
    def isPalindrome(self, s: str) -> bool:
        def character_valid(c: str) -> bool:
            return c.isalpha() or c.isdigit()
        l = 0
        r = len(s) - 1
        

        while l < r:
            while l < r and not character_valid(s[l]):
                l += 1

            while r > l and not character_valid(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        