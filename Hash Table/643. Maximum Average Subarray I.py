class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = sum(nums[0:k])
        tmp = res
        n = len(nums)
        for i in range(k, n):
            tmp = tmp - nums[i - k] + nums[i]
            res = max(res, tmp)

        return res / (k + 0.0)

solution = Solution()
print solution.findMaxAverage([1,12,-5,-6,50,3], 4)