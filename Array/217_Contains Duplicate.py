class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for index in range(len(nums) -1 ):
            if nums[index] == nums[index+1]:
                return True
        return False


solution = Solution()
print solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
