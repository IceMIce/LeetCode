# coding=utf-8
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        【需要看】
        """
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            nums[j] = -abs(nums[j])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

solution = Solution()
print solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])