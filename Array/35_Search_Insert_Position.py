class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1 and nums[0] < target:
            return 1
        elif nums[0] >= target:
            return 0
        elif nums[len(nums)-1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] < target and target <= nums[i + 1]:
                return i + 1

solution = Solution()
print solution.searchInsert([1,3], 3)