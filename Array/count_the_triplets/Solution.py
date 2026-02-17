class Solution:
    def countTriplet(self, arr):
		# code here

        arr.sort()
        n = len(arr)
        out = 0
    
        for i in range(n-1,1,-1):
            l=0
            r=i-1
		    
            while(l<r):
                if(arr[l]+arr[r]==arr[i]):
                   out+=1
                   l+=1
                   r-=1
                elif(arr[l]+arr[r]>arr[i]):
                   r-=1
                else:
                    l+=1
        return out