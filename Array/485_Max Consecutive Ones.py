class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        max_num_list = []
        for num in nums:
            if num == 1:
                i = i + 1
                max_num_list.append(i)
            else:
                i = 0

        if len(max_num_list) == 0:
            return 0

        return max(max_num_list)


solution = Solution()
print solution.findMaxConsecutiveOnes([1])