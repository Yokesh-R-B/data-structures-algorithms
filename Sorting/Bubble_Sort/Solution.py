class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n-1,-1,-1):
            for j in range(0,n-1):
                if(arr[j] > arr[j+1]):
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    
        return arr