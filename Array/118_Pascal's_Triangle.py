class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # @return a list of lists of integers
        ret = []
        for i in range(numRows):
            ret.append([1])
            for j in range(1, i + 1):
                if j == i:
                    ret[i].append(1)
                else:
                    ret[i].append(ret[i - 1][j] + ret[i - 1][j - 1])
        return ret



solution = Solution()
print solution.generate(5)