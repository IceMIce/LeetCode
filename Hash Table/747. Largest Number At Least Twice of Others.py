class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_copy = nums[:]
        if len(nums) == 1:
            return 0
        else:
            nums.sort()
            if nums[-1] >= nums[-2] * 2:
                return nums_copy.index(nums[-1])
            else:
                return -1

solution = Solution()
print solution.dominantIndex([3, 6, 1, 0])