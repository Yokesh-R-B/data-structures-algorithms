class Solution:
    def frequencyCount(self, arr):
        #  code here
    
        result = [0] * len(arr)

        for x in arr:
            result[x-1]+=1
            
        return result