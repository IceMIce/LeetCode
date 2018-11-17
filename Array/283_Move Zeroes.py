class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i = i + 1

        for index in range(len(nums)):
            if index > i - 1:
                nums[index] = 0

solution = Solution()
print solution.moveZeroes([0,1,0,3,12])