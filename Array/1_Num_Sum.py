class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for index, num in enumerate(nums):
            flag = index
            for inner_num in nums[index+1:]:
                flag = flag + 1
                if num + inner_num == target:
                    return [index, flag]


solution = Solution()
print solution.twoSum([-1,-2,-3,-4,-5], -8)