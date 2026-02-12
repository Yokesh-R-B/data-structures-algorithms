class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        
        for x in arr:
            if(x > max):
                max = x
            if(x < min):
                min =x
                
        return[min, max]