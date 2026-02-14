class Solution:
    def missingNum(self, arr):
        # code here
        
        lst = [False] * (len(arr)+2)
        
        for x in arr:
            lst[x] = True
            
        for i in range(1,len(lst)):
            if(lst[i] == False):
                return i
        
        return -1
            
            