class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if i == len(bits)-1:
                if bits[i] == 0:
                    return True
                else:
                    return False
            else:
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
        return False



solution = Solution()
print solution.isOneBitCharacter([1, 0, 0])