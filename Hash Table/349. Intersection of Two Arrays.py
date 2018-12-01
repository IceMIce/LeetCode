class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return_list = []
        for nums in set(nums1):
            if nums in set(nums2):
                return_list.append(nums)
        return return_list
solution = Solution()
print solution.intersection([4,9,5], [9,4,9,8,4])