class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digits = {}
        for num in nums:
            digits[num] = digits.get(num, 0) + 1
            if digits[num] > len(nums) / 2:
                return num


solution = Solution()
print solution.majorityElement([3,2,3])