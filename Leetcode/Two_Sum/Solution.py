class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}

        for i,x in enumerate(nums):
            if((target - x) in s):
                return[s[target-x],i]
            s[x]=i