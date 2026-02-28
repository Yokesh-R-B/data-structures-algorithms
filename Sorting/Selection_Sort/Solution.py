class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        
        for i in range(0,n-1):
            smallest = i
            
            for j in range(i+1,n):
                if(arr[smallest] > arr[j]):
                    smallest = j
            
            arr[smallest], arr[i] = arr[i], arr[smallest]
                    
        return arr