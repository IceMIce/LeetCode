class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        i = length - 1
        while (i >= 0):
            if i == 0:
                if (digits[i] + 1) > 9:
                    digits[i] = 0
                    result = [1]
                    result.extend(digits)
                    return result
            if (digits[i] + 1) <= 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
        return digits


solution = Solution()
print solution.plusOne([1,9,9])