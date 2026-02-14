class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lst = [False]*(len(nums)+2)

        for x in nums:
            if(lst[x] == True):
                return x
            lst[x] = True

        return -1