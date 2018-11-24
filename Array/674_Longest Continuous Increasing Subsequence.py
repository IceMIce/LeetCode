class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(list(set(nums))) <= 1:
            return 1
        start_num = nums[0]
        length = 1
        max_length = []

        for index in range(len(nums)):
            if nums[index] > start_num:
                length = length + 1
                start_num = nums[index]
                max_length.append(length)
            else:
                start_num = nums[index]
                length = 1

        if len(max_length) == 0:
            return 1

        return max(max_length)

solution = Solution()
print solution.findLengthOfLCIS([1,3,5,4,2,3,4,5])
