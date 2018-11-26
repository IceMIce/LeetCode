class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, value in dic.items():
            if value == 1:
                return key
        return 0

solution  = Solution()
print solution.singleNumber([2,2,1])