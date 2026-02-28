class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = 0
        count = 0

        for x in nums:
            if(count == 0):
                cand =x
                count+=1
            else:
                if(cand==x):
                    count+=1
                else:
                    count-=1

        return cand