class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        len_n = len(nums)
        for i in range(len_n):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1

solution = Solution()
print solution.removeDuplicates([1,1,2])