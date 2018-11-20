class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) > nums[len(nums)-1]:
            return len(nums)

        for index in range(len(nums)):
            if index != nums[index]:
                return index


solution = Solution()
print solution.missingNumber([1])