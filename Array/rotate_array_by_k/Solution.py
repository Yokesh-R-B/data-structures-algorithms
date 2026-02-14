class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if(n == 1):
            return nums

        k = k%n

        def reverse(l,r):
                while(l<r):
                    first = nums[l]
                    last = nums[r]
                    nums[l] =last
                    nums[r] = first
                    l+=1
                    r-=1
        
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        

        return nums