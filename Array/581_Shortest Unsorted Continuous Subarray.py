class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort = sorted(nums)
        x = []
        for i in range(len(nums)):
            if nums[i] != sort[i]:
                x.append(i)
        if not x:
            return 0
        else:
            return x[-1] - x[0] + 1

solution = Solution()
print solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])