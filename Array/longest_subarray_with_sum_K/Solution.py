class Solution:
    def longestSubarray(self, arr, k):  
        # code here
    
        sum = 0
        firstSeen = {}
        maxLength = 0
        
        for i,x in enumerate(arr):
            sum += x
            
            if(sum == k):
                maxLength = max(maxLength,i+1)
                
            if((sum - k) in firstSeen):
                l = firstSeen[sum-k]
                maxLength  = max(maxLength , i-l)
                
            if(sum not in firstSeen):
                firstSeen[sum] = i
                
        return maxLength