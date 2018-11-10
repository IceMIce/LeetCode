class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        curr_sum = 0
        max_sum = -2147483647
        for i in range(len(A)):
            if curr_sum < 0 :
                curr_sum = 0
            curr_sum = curr_sum + A[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum



solution = Solution()
print solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])