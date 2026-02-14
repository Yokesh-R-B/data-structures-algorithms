class Solution:
    def twoSum(self, arr, target):
		# code here
        l = 0
        r = len(arr)-1
        arr.sort()
        while(l<r):
            sum = arr[r]+arr[l]
            if(target > sum):
                l+=1
            if(sum>target):
                r-=1
            if(sum == target):
                return True
        
        return False
        