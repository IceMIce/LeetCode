class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters = {}
        for c in s:
            letters[c] = letters[c] + 1 if c in letters else 1
        for c in t:
            if c not in letters:
                return c
            letters[c] -= 1
            if letters[c] < 0:
                return c

solution = Solution()
print solution.findTheDifference("abcd", "abcde")