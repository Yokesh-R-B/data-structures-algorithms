class Solution:
    def kthElement(self, a, b, k):
        # code here
        
        n =len(a)
        m = len(b)
        
        if(m>n):
            return self.kthElement(b,a,k)
        
        lo = max(0, k-m)
        hi = min(k,n)
        
        while (hi>=lo):
            cutA = (lo+hi) // 2
            cutB = k-cutA
            
            leftA = float("-inf") if (cutA ==0) else (a[cutA-1])
            leftB = float("-inf") if (cutB ==0) else (b[cutB-1])
            
            rightA = float("inf") if(cutA == n) else (a[cutA])
            rightB = float("inf") if(cutB == m) else (b[cutB])
            
            if(leftA<= rightB) and (leftB <= rightA):
                return(max(leftA,leftB))
            elif(leftA > rightB):
                hi = cutA-1
            else:
                lo = cutA+1