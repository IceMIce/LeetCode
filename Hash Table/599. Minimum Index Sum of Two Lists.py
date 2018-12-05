class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min = 99999
        ans = []
        for li in list1:
            if li in list2:
                if list1.index(li) + list2.index(li) < min:
                    min = list1.index(li) + list2.index(li)
                    ans = []
                    ans.append(li)
                elif list1.index(li) + list2.index(li) == min:
                    ans.append(li)
        return ans



solution = Solution()
print solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])